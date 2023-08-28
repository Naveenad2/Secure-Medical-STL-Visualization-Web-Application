from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def Login(request):
    return render(request,'store/login.html')


def user_login(request):

     if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=name,password=password)
        print(name,password)
        if user is not None:
            login(request,user)
           
     return main(request)    

@login_required(login_url='/Login')
def main(request):
    category = Model_category.objects.all()
    return render(request,'store/category.html',{'category':category})


@login_required(login_url='/Login')
def models(request,id):

    models_category = Model_category.objects.get(id=id)
    models = Model_details.objects.filter(category=models_category)

    return render(request,'store/models.html',{'model':models})

@login_required(login_url='/Login')
def model_details(request,id):

     models = Model_details.objects.filter(id=id)


     return render(request,'store/model_details.html',{'model':models})

@login_required(login_url='/Login')
def stl(request,id):
    models = Model_details.objects.filter(id=id)
    stl_file_path = None
    for data in models:
        stl_file_path = data.stl_file
    return render(request,'store/stl.html',{'stl_file_path':stl_file_path})