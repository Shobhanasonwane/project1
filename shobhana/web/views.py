from django.shortcuts import render,redirect
from.forms import StudentForms
from.forms import EmployeeForms
from .models import Student,Employee

# Create your views here.
def index(request):
    return render(request,'index.html')

def student(request):
        form = StudentForms
        if request.method == 'POST':
            stud_form = StudentForms(request.POST)
            if stud_form.is_valid():
                stud_form.save()
                return redirect('/list')
        return render(request, 'student.html', {'form': form})


def employee(request):
    form = EmployeeForms
    if request.method == 'POST':
        emp_form = EmployeeForms(request.POST)
        if emp_form.is_valid():
            emp_form.save()
            return redirect('/list1')
    return render(request, 'employee.html', {'form': form})


def student_list(request):
    data = Student.objects.all()
    return render(request, 'studentlist.html', {'data': data})


def employee_list(request):
    data = Employee.objects.all()
    return render(request, 'employeelist.html', {'data': data})

def deletestudent(request,id):
    name=Student.objects.get(id=id)
    name.delete()
    return redirect('/list')

def updatestudent(request,id):
    name=Student.objects.get(id=id)
    form=StudentForms(instance=name)
    if request.method == 'POST':
        saveform=StudentForms(request.POST or None,instance=name)
        if saveform .is_valid():
            saveform.save()
            return redirect('/list')
    return render(request,'updatestudent.html',{'from':form})

def addstudent(request):
    form=StudentForms
    if request.method == 'POST':
        saveform=StudentForms(request.POST)
        if saveform.is_valid():
            saveform.save()
            return redirect('/list')
    return render(request,'addstudent.html',{'form':form})








