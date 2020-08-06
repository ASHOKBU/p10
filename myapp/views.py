from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,"base.html")
def home(request):
    return render(request,"myapp/home.html")
def profile(request):
    name='ASHOK'
    return render(request,"myapp/profile.html",{'name':name})