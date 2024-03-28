from django.shortcuts import render
# Create your views here.
from django.template import loader 
from django.http import HttpResponse
from .models import student_data
#def home(request):
    #students=student_data.objects.all().values()
    #template=loader.get_template('first.html')
    #context={
        #'students':students
   # }
   # return HttpResponse(template.render(context,request))
def home(request):
    students=student_data.objects.all()
    if request.method =='POST':
       first_name=request.POST.get("firstname")
       last_name=request.POST.get("Lastname")
       email=request.POST.get("email")
       gender=request.POST.get("gender")
       student_data.objects.create(
           first_name=first_name,
           last_name=last_name,
           email=email,
           gender=gender
           )
       return HttpResponse("Data added Successfully.<a href='/first.html'>Go back</a>")
    return render(request,'first.html',{'students':students})