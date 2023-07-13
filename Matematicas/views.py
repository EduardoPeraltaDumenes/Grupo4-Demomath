from django.shortcuts import render,HttpResponse


def home_view(request):
    return render(request, 'home.html')


def demo1_view(request):
    return render(request, 'demo1.html')

def demo2_view(request):
    return render(request, 'demo2.html')


def demo3_view(request):
    return render(request, 'demo3.html')
