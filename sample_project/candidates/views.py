from django.shortcuts import render,redirect
from candidates.models import Login
from candidates.models import SignUp
from candidates.models import Attendance
from django.contrib import messages



def Home_Page(request):
    return render(request,"Homepage.html")

def DASHBOARD(request):
    return render(request,"Dashboard.html")

def Allotment(request):
    return render(request,"index.html")

def Payment_Page(request):
    return render(request,"Payment.html")

def VR(request):
    return render(request,"vr.html")


def SignUp_Page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        if Login.objects.filter(email = email).exists():
            messages.warning(request,'email already exists')
        else:
            instance = Login(name = name, email = email, password = password)
            instance.save()
            messages.success(request,"User has been registered successfully")
            return DASHBOARD(request)
    return render(request,'SignUp.html')


def Login_Page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if Login.objects.filter(email = email, password = password): 
            return DASHBOARD(request)
        else:
            messages.warning(request,'Incorrect email or password')
            return render(request,'Login.html')
    return render(request,'Login.html')


def Attendance_Page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        candidate_id = request.POST.get('candidate_id')
        if Attendance.objects.filter(candidate_id = candidate_id).exists(): 
            messages.warning(request,'User already Exists')
            return DASHBOARD(request)
        else:
            instance = Attendance(name = name, candidate_id = candidate_id)
            instance.save()
            messages.success(request,'Student Added Successfully')
            return render(request,'Attendance.html')
    return render(request,'Attendance.html')
