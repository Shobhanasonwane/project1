from django.forms import ModelForm
from.models import Student,Employee

class StudentForms (ModelForm):
    class Meta:
        model=Student
        fields='__all__'


from.models import Employee

class EmployeeForms (ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
