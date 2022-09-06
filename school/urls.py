from django.urls import path
from . import views
urlpatterns = [
# path('statistic/students', views.statistic_student,name='statistic_student'),
    path('', views.statistic_student, name='statistic_student'),
    #----------classes-----------
path('classes', views.list_class,name='classes'),
path('class/add', views.add_class,name='add_class'),
path('class/update/<int:id>', views.update_class,name='update_class'),
path('class/<int:id>/delete', views.delete_class,name='delete_class'),

#----------countries-----------
path('countries', views.list_country,name='countries'),
path('country/add', views.add_country,name='add_country'),
path('country/update/<int:id>', views.update_country,name='update_country'),
path('country/<int:id>/delete', views.delete_country,name='delete_country'),

#----------students-----------
path('students', views.list_student,name='students'),
path('student/add', views.add_student,name='add_student'),
path('student/update/<int:id>', views.update_student,name='update_student'),
path('student/<int:id>/delete', views.delete_student,name='delete_student'),

]
