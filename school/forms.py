from django import forms
from .models import Country,Class,Student
from .widget import DatePickerInput,DateTimePickerInput,TimePickerInput
class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('class_name',)

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

class StudentForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DatePickerInput)

    class Meta:
        model = Student
        fields = ('name','date_of_birth','Class','Country',)


