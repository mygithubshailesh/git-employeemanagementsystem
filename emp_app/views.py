from django.shortcuts import render


def index(request):
    return render (request,'index.html')

def all_employee(request):
    return render (request,'veiw_all_emp.html')

def add_employee(request):
    return render (request,'add_all_emp.html')

def remove_employee(request):
    return render (request,'remove_all_emp.html')

def filter_employee(request):
    return render (request,'filter_all_emp.html')


