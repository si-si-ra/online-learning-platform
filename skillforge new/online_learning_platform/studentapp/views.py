import os
from django.shortcuts import render,redirect

# from django.contrib.auth.decorators import login_required
from.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def student_dashboard(request):
    return render(request,'studentapp/student_dashboard.html')

def all_course(request):
    return render(request,'studentapp/all_course.html')


def student_register(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)

            return redirect('student_login')
    context={'form':form}
    return render(request,'studentapp/student_register.html',context)


def student_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('student_dashboard')
        else:
            messages.info(request,'Username or Password is incorrect')
            return render(request,'studentapp/student_login.html')

    return render(request,'studentapp/student_login.html')

def student_logout(request):
    logout(request)
    return redirect('studentapp/student_login.html')

def python_course(request):
    return render(request,'studentapp/python_course.html')
def fullstack_course(request):
    return render(request,'studentapp/fullstack_course.html')



# views.py
from django.http import HttpResponse
from .forms import CertificateForm
from reportlab.pdfgen import canvas

from online_learning_platform import settings

def certificate_upload(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            course_name = form.cleaned_data['course_name']

            # Create the PDF certificate
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'

            # Create PDF content
            pdf = canvas.Canvas(response)
            pdf.drawString(100, 750, "Course Completion Certificate")
            pdf.drawString(100, 700, f"Name: {full_name}")
            pdf.drawString(100, 650, f"Course: {course_name}")
            pdf.showPage()
            pdf.save()

            file_path = os.path.join(settings.MEDIA_ROOT, 'certificate.pdf')
            print("PDF saved at:", file_path)


            return response
    else:
        form = CertificateForm()
    return render(request, 'studentapp/certificate_upload.html', {'form': form})

