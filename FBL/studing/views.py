from django.shortcuts import render
from django.http import HttpResponse

def page_1(request):
    return render(request, 'studing/page_1.html')

def page_2(request):
    return render(request, 'studing/page_2.html')

def page_3(request):
    return render(request, 'studing/page_3.html')

def page_4(request):
    return render(request, 'studing/page_4.html')

def page_5(request):
    return render(request, 'studing/page_5.html')

def page_6(request):
    return render(request, 'studing/page_6.html')