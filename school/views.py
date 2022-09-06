from django.shortcuts import render, redirect, get_object_or_404
from .models import Class, Country, Student
from django.db.models import Q
from .forms import ClassForm, CountryForm, StudentForm
from django.contrib import messages
from django.urls import reverse

from datetime import date
from django.utils.timezone import now


def index(request):
    return render(request, 'pages/index.html', {})


# ----------classes-----------
def list_class(request):
    classes = Class.objects.all()

    context = {
        'classes': classes,

    }
    return render(request, 'pages/classes/list_classes.html', context)


# ************add class***********
def add_class(request):
    form = ClassForm()
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'class added successfully')
            return redirect('classes')

    context = {
        'form': form
    }
    return render(request, 'pages/classes/add_class.html', context)


# ************update class***********
def update_class(request, id):
    Class_ = Class.objects.get(pk=id)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=Class_)
        if form.is_valid():
            form.save()
            messages.success(request, 'class updated successfully')
            return redirect('classes')
    else:
        form = ClassForm(instance=Class_)

    context = {
        'form': form
    }
    return render(request, 'pages/classes/edit_class.html', context)


# ************delete class***********
def delete_class(request, id):
    class_obj = get_object_or_404(Class, id=id)
    if request.method == 'POST':
        class_obj.delete()
        messages.error(request, 'class deleted successfully')
        return redirect('classes')
    context = {
        'class': class_obj
    }
    return render(request, 'pages/classes/delete_class.html', context)


# ----------country-----------
def list_country(request):
    countries = Country.objects.all()
    context = {
        'countries': countries,
    }
    return render(request, 'pages/countries/list_countries.html', context)


# ************add country***********
def add_country(request):
    form = CountryForm()
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Country added successfully')

            return redirect('countries')

    context = {
        'form': form
    }
    return render(request, 'pages/countries/add_country.html', context)


# ************update country***********
def update_country(request, id):
    country_obj = Country.objects.get(id=id)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country_obj)
        if form.is_valid():
            form.save()
            messages.success(request,'Country updated successfully')

            return redirect('countries')
    else:
        form = CountryForm(instance=country_obj)

    context = {
        'form': form
    }
    return render(request, 'pages/countries/edit_country.html', context)


# ************delete country***********
def delete_country(request, id):
    country_obj = get_object_or_404(Country, id=id)
    if request.method == 'POST':
        country_obj.delete()
        messages.error(request, 'Country deleted successfully')

        return redirect('countries')
    context = {
        'country': country_obj
    }
    return render(request, 'pages/countries/delete_country.html', context)


# ----------student-----------
def list_student(request):
    students = Student.objects.all()
    classes = Class.objects.all()
    countries = Country.objects.all()

    context = {
        'students': students,
        'classes': classes,
        'countries': countries
    }
    return render(request, 'pages/students/list_students.html', context)


# ----------student-----------
# ************add student***********
def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'student deleted successfully')
            return redirect('students')

    context = {
        'form': form
    }
    return render(request, 'pages/students/add_student.html', context)


# ************update student***********
def update_student(request, id):
    student_obj = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'student updated successfully')

            return redirect('students')
    else:
        form = StudentForm(instance=student_obj)

    context = {
        'form': form
    }
    return render(request, 'pages/students/edit_student.html', context)


# ************delete student***********
def delete_student(request, id):
    student_obj = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student_obj.delete()
        messages.error(request, 'student deleted successfully')

        return redirect('students')
    context = {
        'student': student_obj
    }
    return render(request, 'pages/students/delete_student.html', context)


# ************statistic student***********

def statistic_student(request):
    classes = Class.objects.all()

    countries = Country.objects.all()
    class_labels = []
    class_student_data = []

    for class_ in classes:
        class_labels.append(class_.class_name)

        class_student_count = len(Student.objects.filter(Q(Class=class_)))

        class_student_data.append(class_student_count)
        class_labels_count = len(class_labels)
        class_studentlist = zip(class_labels, class_student_data)

    country_labels = []
    country_student_data = []
    for country in countries:
        country_labels.append(country.name)
        country_student_count = len(Student.objects.filter(Q(Country=country)))
        country_student_data.append(country_student_count)
        country_labels_count = len(country_labels)
        country_studentlist = zip(country_labels, country_student_data)

    students = Student.objects.all()
    students_age = []
    for student in students:
        today = date.today()
        age = today.year - student.date_of_birth.year - (
                (today.month, today.day) < (student.date_of_birth.month, student.date_of_birth.day))
        students_age.append(age)
        print(students_age)


    import math
    average_age = math.ceil(sum(students_age) / len(students_age))
    return render(request, 'pages/students/statistic_student.html', {
        'class_studentlist': class_studentlist,
        'average_age': average_age,
        'class_labels': class_labels,
        'class_student_data': class_student_data,
        'class_labels_count': class_labels_count,
        'country_studentlist': country_studentlist,
        'country_labels': country_labels,
        'country_student_data': country_student_data,
        'country_labels_count': country_labels_count,
    })
