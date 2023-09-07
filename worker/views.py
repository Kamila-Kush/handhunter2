from django.shortcuts import render
from .models import Worker, Resume

def worker_list(request):
    workers = Worker.objects.all()
    context = {'workers': workers}
    return render(request, 'workers.html', context)

def worker_detail(request, id):
    worker_object = Worker.objects.get(id=id)
    resume_object = Resume.objects.get(id=id)
    context = {'worker': worker_object,
               'resume': resume_object
               }
    return render(request, 'worker-detail.html', context)
