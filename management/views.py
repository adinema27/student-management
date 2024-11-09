from django.shortcuts import render, redirect, HttpResponse
from management.models import student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        name  = request.POST.get("first_name")
        last_name = request.POST.get('last_name')
        user = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('password')
        obj = User(first_name = name, last_name = last_name, username = user, email = email)
        obj.set_password(password) 
        obj.save()
        print(obj)
    return render (request, 'register.html')

def login_user (request):
    if request.method == "POST":
        user = request.POST.get('user')
        password = request.POST.get('password')
        obj = authenticate(request, username= user, password = password)
        print(obj)
        if obj is not None:
            login(request, obj)
            return redirect('home')
        else:
            return HttpResponse('User Not Found, Please Register')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def home (request):
    students = student.objects.filter(fk = request.user)
    data = {
        'students': students
    }
    return render(request, 'home.html', context=data)


@login_required
def add(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        name = request.POST.get('name')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        student.objects.create(fk = request.user, email=email, contact = contact,name=name, age = age, dob = dob)
        
        return redirect('home')
    return render(request, 'add.html')

def update(request,pk):
    data = student.objects.get(id = pk)
    if request.method == 'POST':
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        name = request.POST.get('name')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        data.email = email
        data.contact = contact
        data.name = name 
        data.age = age 
        data.dob = dob
        data.save()
        return redirect('home')
    students = {
        'data': data
    }
    
    return render(request, 'update.html', context=students)


def delete(request, pk):
    task = student.objects.get(id=pk)
    task.delete()
    return redirect('home')


def history(request):
    return render(request, 'history.html')