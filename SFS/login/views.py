from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login/')
def home(request):
	return render(request,"home.html")


def base(request):
	return render(request,"base.html")


# Create your views here.

