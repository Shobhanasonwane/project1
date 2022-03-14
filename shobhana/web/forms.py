from django.forms import ModelForm
from.models import student,Employee

class StudentForms (ModelForm):
    class Meta:
        model=student
        fields='__all__'


from.models import Employee

class EmployeeForms (ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
