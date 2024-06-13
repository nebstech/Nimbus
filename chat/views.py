from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Room

@csrf_exempt
def create_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        if not room_name:
            return JsonResponse({'error': 'Room name is required'}, status=400)
        room, created = Room.objects.get_or_create(name=room_name)
        return JsonResponse({'room_name': room_name, 'created': created})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
