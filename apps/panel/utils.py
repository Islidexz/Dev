import bleach
from config.base import MEDIA_DIR
import os
from django.utils.timezone import now
from django.core.files.uploadedfile import InMemoryUploadedFile
import io
from apps.panel.panel_config import *

def process_svg(file):
    sanitized_content = sanitize_svg(file.read().decode())
    return InMemoryUploadedFile(
        io.BytesIO(sanitized_content.encode()),
        field_name='file',
        name=file.name,
        content_type='image/svg+xml',
        size=len(sanitized_content),
        charset='utf-8'
    )

def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    year_month = now().strftime('%Y/%m')
    directory_path = os.path.join('media', year_month, ext)  
    return os.path.join(directory_path, filename)
    # return os.path.join('media', year_month, filename)

def sanitize_svg(svg_content):
    return bleach.clean(svg_content, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRS, strip=True)

def get_upload_path(instance, filename):
    # Get the file extension and check if it's in the allowed formats
    file_extension = os.path.splitext(filename)[1].lower().replace('.', '')
    if file_extension in ALLOWED_IMAGE_FORMATS:
        # Here you can customize the folder name based on the file format if needed
        folder_name = 'SVG' if file_extension == 'svg' else 'images'
        # Assuming you have a slug or some unique identifier for the instance
        new_filename = f"{instance.url}.{file_extension}"
        return os.path.join(MEDIA_DIR, folder_name, new_filename)
    else:
        raise ValueError(f"File format '{file_extension}' is not allowed.")
    

