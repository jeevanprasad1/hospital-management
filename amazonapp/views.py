from django.shortcuts import render
from django.http import HttpResponse
from . models import Department
from . models import *
from . forms import BookingForm
# Create your views here.
# def index(requaest):
#     return HttpResponse("hello world")
# def index(request):
#     return render (request,"index.html")
# def booking(requaest):
#     return HttpResponse("booking page")
# def doctors(requaest):
#     return HttpResponse("doctors page")
# def about(requaest):
#     return HttpResponse("about page")
# def index(request):
#     return render (request,"index.html")
# def doctors(request):
#     return render (request,"doctors.html")
# def booking(request):
#     return render (request,"booking.html")
# def about (request):
#     return render (request,"about.html")
def index(request):
 person={
    'name':'jeevan',
    'age':18,
     'num1':10
 }
 numbers={
        'num1':[1,2,3,4,5,6,7]
    }
 return render(request,"index.html",numbers)

def about(request):
    return render(request,"about.html")
def booking(request):
    # return render(request,"booking.html")
    if request.method =='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form=BookingForm
    dict_form={
    'form':form
}
    return render(request,"booking.html",dict_form)

def doctors(request):
    return render(request,"doctors.html")
def contact(request):
    return render(request,"contact.html")
def department(request):
    return render(request,"department.html")

def department(request):
    dict_dep={
        'dept':Department.objects.all()

    }
    return render(request, 'department.html',dict_dep)

def doctors(request):
    dict_doc={
        'doctors':Doctors.objects.all()

    }
    return render(request, 'doctors.html',dict_doc)




