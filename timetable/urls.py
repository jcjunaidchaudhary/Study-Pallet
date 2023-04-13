from django.urls import path
from timetable import views 

urlpatterns=[
    # path('faculty',views.faculty,name='add_Faculty'),
    path('',views.index,name='home'),
    path('course/',views.course,name='course'),
    path('rooms/',views.rooms,name='room'),
    path('sem/',views.sem,name='sem'),
    path('time-slot/',views.time,name='time'),
    path('generate-timetable/',views.timetable,name='generate-timetable'),
    path('generate-timetable/timetable-docx/',views.timetable_docx,name='timetable-docx'),
    path('generate-timetable/timetable-pdf/',views.timetable_pdf,name='timetable-pdf'),
]
