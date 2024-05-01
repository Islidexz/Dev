import bleach

STATE_CHOICES = (('active', 'Active'), ('inactive', 'Inactive')); 
TYPE_CHOICES = (('cat', 'Category'), ('page', 'Page'),('tpl', 'HTML Template'), ('price', 'Price'), ('gallery', 'Gallery'))
###
IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png']
SVG_EXTENSIONS = ['svg']
DOCUMENT_EXTENSIONS = ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx']
ALLOWED_EXTENSIONS = IMAGE_EXTENSIONS + SVG_EXTENSIONS + DOCUMENT_EXTENSIONS
# Convert TAGS list to a set
TAGS = {'svg', 'g', 'path', 'circle', 'line', 'rect', 'text', 'polyline', 'polygon'}
ALLOWED_TAGS = set(bleach.sanitizer.ALLOWED_TAGS) | TAGS
ALLOWED_TAGS = frozenset(ALLOWED_TAGS)
ALLOWED_IMAGE_FORMATS = ['svg', 'jpg', 'jpeg', 'png', 'gif']

# Define the ALLOWED_ATTRIBUTES, including SVG-specific attributes
ALLOWED_ATTRS = bleach.sanitizer.ALLOWED_ATTRIBUTES
ALLOWED_ATTRS.update({
    '*': ['class', 'id', 'style'],
    'path': ['d'],
    'text': ['x', 'y'],
    'polyline': ['points'],
    'polygon': ['points'],
    'svg': ['width', 'height'],
    'g': ['transform'],
    'circle': ['cx', 'cy', 'r'],
    'line': ['x1', 'y1', 'x2', 'y2'],
    'rect': ['x', 'y', 'width', 'height'],
    'image': ['xlink:href'],
    'a': ['href', 'target', 'rel'],
    'use': ['xlink:href'],
})