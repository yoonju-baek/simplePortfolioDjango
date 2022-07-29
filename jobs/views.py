from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'jobs/home.html')

def project1(request):
    return render(request, 'jobs/project1.html')

def project2(request):
    return render(request, 'jobs/project2.html')

def project3(request):
    return render(request, 'jobs/project3.html')