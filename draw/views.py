# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def upload(request):
    return render(request, 'draw/upload.html')

def repartee(request):
    return render(request, 'draw/repartee.html')
    
def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })