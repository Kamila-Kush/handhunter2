from django.shortcuts import render
from .models import Company

def company_list(request):
    companies = Company.objects.all()
    context = {'companies': companies}
    return render(request, 'company-list.html', context)

def company_detail(request, id):
    company = Company.objects.get(id=id)
    employee = company.employee.all()
    return render(
        request,
        'company-detail.html',
        {
            'company': company,
            'employee': employee
        }
    )