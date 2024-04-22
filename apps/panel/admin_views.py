from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

def get_objects(request):
    content_type_id = request.GET.get('content_type')    # Get the content_type ID from the GET request parameters
    serialized_objects = []    # Initialize an empty list for serialized objects
    try:
        content_type = ContentType.objects.get_for_id(int(content_type_id))        # Convert the ID to an integer and fetch the corresponding ContentType
        model = content_type.model_class()        # Get the model class associated with this ContentType
        objects = model.objects.all()        # Fetch all objects of this model (you may want to apply filters or order them)
        serialized_objects = [{'id': obj.id, 'name': str(obj)} for obj in objects]        # Serialize the objects into a list of dictionaries
    except (ValueError, ObjectDoesNotExist):        # If the content_type_id is not valid or no ContentType is found, handle the exception
        pass
    return JsonResponse({'objects': serialized_objects})    # Return the serialized objects as a JSON response
