from django.shortcuts import render
from .models import *

def home(request):
    obj1= Student.objects.all()
    obj2= Teacher.objects.all()
    obj3= Employee.objects.all()
    obj4= Customer.objects.all()
    return render(request,'index.html',{'obj1':obj1, 'obj2':obj2, 'obj3':obj3, 'obj4':obj4})
