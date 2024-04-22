from django.contrib import admin
#from .models import Slice, Page, Media
from .models import Slice
from .models import Media
from django.utils.html import format_html


class MediaInline(admin.TabularInline):
    model = Media
    extra = 1
    fields = ('title', 'file', 'file_type', 'file_size',) # Убедитесь, что 'uploaded_at' здесь нет
    readonly_fields = ('image_preview', 'uploaded_at') # 'uploaded_at' может быть указано здесь, если должно отображаться, но быть неизменяемым

    def image_preview(self, obj):
        if obj.media.file:  # Assuming 'media' has a 'file' attribute
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.media.file.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'

class SliceInline(admin.TabularInline):
    model = Slice
    extra = 1
    fields = ('title', 'state', 'price', 'text', 'icon', 'img')  # Поля, выбранные на основе вашей модели 'Slice'
    readonly_fields = ('timestamp',)  # Если вы хотите, чтобы поле 'timestamp' было доступно только для чтения