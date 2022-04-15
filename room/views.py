from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Message, Room

# Create your views here.
# Import the Room database model

# View for the rooms
@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})


def room(request, pk):
    room = Room.objects.get(id=pk)
    messages = Message.objects.filter(room__id=room.id)[0:25]
    return render(request, 'room/room.html', {'room': room, 'messages': messages})
