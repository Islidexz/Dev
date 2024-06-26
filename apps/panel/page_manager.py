from mptt.models import MPTTModel, TreeManager;from functools import wraps
from typing import Dict, List, Any
from django.core.cache import cache
###
import logging; import time; import cProfile, pstats; from io import StringIO;
from django.utils.functional import cached_property
from config.base import *


MODEL_CACHE_CONFIG = {
    'page': ['id', 'title', 'text', 'url', 'parent_id', 'level', 'type'],
    'slice': ['id', 'parent_page', 'state', 'title', 'is_main', 'price', 'text', 'timestamp', 'icon', 'img'],
}


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def build_debug_tree(page_data, indent=0):
    """
    Выводит иерархическое дерево страниц в консоль для отладки.
    Рекурсивно обходит детей каждой страницы, увеличивая отступ для вложенных элементов.
    """
    print(' ' * indent + f"Title: {page_data['title']}, URL: {page_data['url']}")
    for child in page_data.get('children', []):
        build_debug_tree(child, indent + 2)

def ensure_cache(func):
    """
    Декоратор для методов менеджера страниц. Проверяет инициализирован ли кэш страниц.
    Если нет, вызывает метод cache_active_pages для кэширования страниц.
    Замеряет время выполнения функции и логирует его.
    """
    @wraps(func)
    def wrapper(manager, *args, **kwargs):
        start_time = time.time()
        if manager.cached_pages is None:
            logger.info(f"Cache miss for {func.__name__}, caching active pages.")
            manager.cache_active_pages()
        else:
            logger.info(f"Cache hit for {func.__name__}, using cached pages.")
        result = func(manager, *args, **kwargs)
        total_time = time.time() - start_time
        logger.info(f"Function {func.__name__} took {total_time:.2f} seconds.")
        return result
    return wrapper



def wrapper(func):
    def cache_wrapper(manager, *args, **kwargs):
        cache_key = f"{func.__name__}_{args}_{kwargs}"
        if result := cache.get(cache_key):
            return result
        result = func(manager, *args, **kwargs)
        cache.set(cache_key, result, timeout=300)  # кэш на 5 минут
        return result
    return cache_wrapper

class PageManager(TreeManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cached_pages = None

    def cache_active_pages(self):
        logger.info("Caching active pages.")
        all_pages = self.get_queryset().filter(state='active').prefetch_related('slices', 'children').order_by('tree_id', 'lft')
        # Use a single comprehension to build both caches
        self.cached_pages = {}
        self.cached_root_nodes = {}
        for page in all_pages:
            self.cached_pages[page.url] = page
            if page.level == 0:
                self.cached_root_nodes[page.url] = page
        logger.debug(f"Cached pages: {list(self.cached_pages.keys())}")
  
    @ensure_cache
    def get_page_by_url(self, url):
        page = self.cached_pages.get(url)
        if not page:
            logger.debug(f"Page not found in cache for URL '{url}', querying the database.")
            page = self.get_queryset().filter(url=url).first()
        return page
            
    def clear_cache(self):
        self.cached_pages = None; logger.info("Clearing page cache.")

    def rebuild_tree(self):
        logger.info(f"Rebuilding MPTT tree for {self.model.__name__}.");self.model.objects.rebuild()
        self.clear_cache();logger.info("MPTT tree rebuild complete.")
    
    def extract_url(self, full_url: str) -> str:
        return full_url.strip('/').split('/')[-1]

    def build_menu(self) -> List[Dict[str, Any]]:
        """
        Строит список элементов меню из кэшированных страниц, используя _build_menu_item для каждой корневой страницы.
        """
        # ...        
        return [self._build_menu_item(page) for page in self.cached_pages.values() if page.level == 0]
    
    def _build_menu_item(self, page) -> Dict[str, Any]:
        logger.debug(f"Building menu item for page: {page.title} (URL: {page.url})")
        # Если страница есть в кэше, получаем дочерние элементы из кэша
        if self.cached_pages and page.url in self.cached_pages:
            children_pages = self.cached_pages[page.url].children.all()
        else:
            # Если нет, получаем дочерние элементы из базы данных
            children_pages = page.get_children()
        return {
            'title': page.title,
            'full_url': self._build_url(page),
            'level': page.level,
            'children': [self._build_menu_item(child) for child in children_pages]
        }
    
    #@cached_property # Cache the URL for each page 
    def _build_url(self, page) -> str:
        """
        Строит полный URL для страницы, используя кэшированные данные предков страницы.
        Если URL не скэширован, выполняет его построение и добавляет в кэш.
        """
        if not hasattr(self, 'cached_ancestors'):
            self.cached_ancestors = {}
        full_url = self.cached_ancestors.get(page.url)
        if not full_url:
            ancestors = (self.cached_pages.get(page.url, page).get_ancestors(include_self=True)
            if self.cached_pages else page.get_ancestors(include_self=True))
            full_url = '/' + '/'.join(ancestor.url.strip('/') for ancestor in ancestors)
            self.cached_ancestors[page.url] = full_url  # Cache the built URL
        return full_url
    

    @ensure_cache
    def build_breadcrumbs(self, page) -> List[Dict[str, Any]]:
        """
        Строит хлебные крошки для страницы, используя её предков.
        REDO: Use the 'cached_ancestors' cache instead of 'get_ancestors'
        """
        breadcrumbs = []
        while page:
            breadcrumbs.append({'title': page.title, 'full_url': self._build_url(page), 'level': page.level})
            page = page.parent  # Assumes 'parent' is the ForeignKey to the parent page
        return list(reversed(breadcrumbs))


    @ensure_cache
    @wrapper
    def to_dict(self, node, include_children=False, include_slices=False, include_siblings=False):
        """
        Конвертирует узел (страницу или срез) в словарь, включающий заданные поля и возможные связи.
        Параметры include_children, include_slices и include_siblings указывают,
        нужно ли включать в словарь дочерние элементы, срезы и соседние узлы соответственно.
        Декоратор @ensure_cache обеспечивает использование кэшированных данных для ускорения работы.
        
        :param node: Объект страницы или среза, который нужно преобразовать.
        :param include_children: Флаг, включать ли дочерние узлы в результат.
        :param include_slices: Флаг, включать ли срезы в результат.
        :param include_siblings: Флаг, включать ли соседние узлы в результат.
        :return: Словарь с данными узла.
        """    
        from .models import Page, Slice
        model_type = 'page' if isinstance(node, Page) else 'slice' if isinstance(node, Slice) else None
        if not model_type:
            logger.error(f"Unsupported node type: {type(node)}")
            return {}
        
        logger.debug(f"Processing node of type: {model_type} with ID: {node.pk}")
        fields = MODEL_CACHE_CONFIG.get(model_type, [])
        data = {field: getattr(node, field, None) for field in fields}
        
        if model_type == 'page':        # Build full URL for the page and include it in the data
            data['full_url'] = self._build_url(node); logger.debug(f"Full URL: {data['full_url']}")
            data['parent'] = self.to_dict(node.parent, False, False, False) if node.parent_id else None
            if include_children:
                children = node.get_children() if not self.cached_pages else self.cached_pages.get(node.url, node).get_children()
                data['children'] = [self.to_dict(child, True, include_slices, False) for child in children]
            if include_slices:
                slices = node.slices.all() if not self.cached_pages else self.cached_pages.get(node.url, node).slices.all()
                data['slices'] = [self.to_dict(slice, False, False, False) for slice in slices]
            if include_siblings and node.parent_id:
                siblings = node.parent.get_children() if not self.cached_pages else self.cached_pages.get(node.parent.url, node.parent).get_children()
                data['siblings'] = [self.to_dict(sibling, False, include_slices, False) for sibling in siblings if sibling.id != node.id]
        return data



    def build_page_context(self, url: str, page=None) -> Dict[str, Any]:
        """
        Построение контекста для страницы по URL. 
        Включает данные страницы, меню, хлебные крошки, уровень и тип текущей страницы.
        ТУДУ: улучшить кэширование
        """        
        cache_key = f"page_context_{url}" # Cache key for the context 
        context = cache.get(cache_key) # Try to get the context from the cache
        current_page = page or self.get_page_by_url(url)
        if current_page is None: 
            error_msg = f"No page found for URL '{url}'."
            logger.error(error_msg)
            raise self.model.DoesNotExist(error_msg)

        page_data = self.to_dict(current_page, include_children=True, include_slices=True, include_siblings=True)        
        page_data.setdefault('slices', [])  # Ensure slices is a list
        breadcrumbs = self.build_breadcrumbs(current_page) if current_page else []

        context = {
                'page_data': page_data,
                'menu_items': self.build_menu(),
                'breadcrumbs': breadcrumbs,
                'current_level': current_page.level,
                'current_page_type': current_page.type,
                # Now use 'parent' directly from 'page_data', which is the actual Page object
                'parent': page_data['parent'],
                # Use siblings directly from 'page_data'
                'siblings': page_data.get('siblings', []),
            }
        #logger.debug(f"Current page title: {current_page.title}")
        cache.set(cache_key, context)

        build_debug_tree(page_data, 0) # Вывод в консоль для отладки
        return context

