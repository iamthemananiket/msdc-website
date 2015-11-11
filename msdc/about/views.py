from django.shortcuts import render

# Create your views here.

def show_aboutpage(request):
    return render(request,'about/about-page.html')
