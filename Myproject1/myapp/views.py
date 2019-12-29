from django.shortcuts import render, redirect
from myapp.Forms import EmployeeForm
from myapp.models import Employee

# Create your views here.
def emp(request):
    if request.method == "POST":
        Myform = EmployeeForm(request.POST, request.FILES)
        if Myform.is_valid():
            Myform.save()
            return redirect(show)
    else:
        Myform = EmployeeForm()
        return render(request, "index.html", {'Myform': Myform})

def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'emplo': employees})
def edit(request,id):
    employee = Employee.objects.get(id=id)
    return render(request, "edit.html", {'employee': employee})
def update(request,id):
    employee = Employee.objects.get(id=id)
    Myform = EmployeeForm(request.POST, request.FILES, instance = employee)
    if Myform.is_valid():
        Myform.save()
        return redirect(show)
    return render(request, "edit.html", {'employee': employee})

def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect(show)







