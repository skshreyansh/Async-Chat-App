from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def room(request,room):
    return render(request,'chatroom.html',{
        'room_name':room
    })