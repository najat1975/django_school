from django.contrib import admin
from .models import Student,Class,Country

admin.site.register(Class)
admin.site.register(Country)
admin.site.register(Student)

# Register your models here.
