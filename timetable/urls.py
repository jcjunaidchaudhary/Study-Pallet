from django.urls import path
from timetable import views 

urlpatterns=[
    path('faculty',views.faculty,name='add_Faculty'),
    path('course',views.course,name='add_Course'),
    path('rooms',views.rooms,name='add_Room'),
    path('sem',views.sem,name='add_Sem'),
    path('time',views.time,name='time'),
    path('generate-timetable',views.timetable,name='generate-timetable'),
]
