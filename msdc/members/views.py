from django.shortcuts import render

from .models import Member

# Create your views here.
def show_member_page(request):
    context = {'members':Member.objects()}
    return render(request,'members/member_page.py',context)
