# chat/views.py
#copy/pasted from: https://channels.readthedocs.io/en/latest/tutorial/part_1.html
#& https://channels.readthedocs.io/en/latest/tutorial/part_2.html
from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    current_user = str(request.user)
    args = {'room_name': room_name}
    return render(request, 'chat/room.html', args)
