from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def set_cookie(request):
    response = HttpResponse("Cookies must be stored!")
    response.set_cookie('username','vineetha')
    return response
def get_cookie(request):
    username =  request.COOKIES.get('username','Guest')
    return HttpResponse(f"Hello, {username}!")
