'''chat/views.py
adapted from: https://channels.readthedocs.io/en/latest/tutorial/part_1.html
& https://channels.readthedocs.io/en/latest/tutorial/part_2.html'''
from django.shortcuts import render

rooms = set()

def index(request):
    '''the index page, basic HTML page for joining a room'''
    return render(request, 'chat/index.html', {'rooms': rooms})

def room(request, room_name):
    '''gets the requested room name, sends that information over
    to the room.html file to build the room page'''
    args = {'room_name': room_name}
    rooms.add(room_name)
    return render(request, 'chat/room.html', args)
