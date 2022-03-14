from django.shortcuts import render,redirect
from.forms import StudentForms
from.forms import EmployeeForms
# Create your views here.
def index(request):
    return render(request,'index.html')

def student(request):
        form = StudentForms
        if request.method == 'POST':
            stud_form = StudentForms(request.POST)
            if stud_form.is_valid():
                stud_form.save()
                return redirect('/student')
        return render(request, 'student.html', {'form': form})


def Employee(request):
    form = EmployeeForms
    if request.method == 'POST':
        emp_form = EmployeeForms(request.POST)
        if emp_form.is_valid():
            emp_form.save()
            return redirect('/Employee')
    return render(request, 'Employee.html', {'form': form})
