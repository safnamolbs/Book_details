from django import forms
from work.models import Emp
from work.models import book
from work.models import Movies
from work.models import Person
from work.models import Mobile
from work.models import Students

class EmpForm(forms.Form):
    name=forms.CharField()
    place=forms.CharField()
    salary=forms.CharField()
    contact=forms.CharField()


class bookForm(forms.ModelForm):
    class Meta:
        model=book
        fields='__all__'

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields='__all__'

class PersonForm(forms.ModelForm):
     class Meta():
         model=Person
         fields='__all__'   

class MobileForm(forms.ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'         

class StudentForm(forms.ModelForm):
    class Meta():
        model=Students
        fields='__all__'
