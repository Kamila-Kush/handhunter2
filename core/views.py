from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request=request, template_name="index.html")

def about_us(request):
    return render(request=request, template_name='about_us.html')