from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def set_session(request):
    request.session['username']='vineetha'
    return  HttpResponse("Session data set!")
    return response
def get_session(request):
    username =  request.session.get('username','Guest')
    return HttpResponse(f"Hello, {username}!")