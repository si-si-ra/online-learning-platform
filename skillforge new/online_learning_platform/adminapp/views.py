from django.shortcuts import render

def home(request):
    return render(request,'adminapp/home.html')

def aboutus(request):
    return render(request,'adminapp/aboutus.html')

def courses(request):
    return render(request,'adminapp/courses.html')

def contact(request):
    return render(request,'adminapp/contact.html')

def courses_icon(request):
    return render(request,'adminapp/courseicon.html')

