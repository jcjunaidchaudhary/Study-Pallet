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
    path('timetable-docx/',views.timetable_docx,name='timetable-docx'),
    path('timetable-pdf/',views.timetable_pdf,name='timetable-pdf'),
    path('delete_sem/<int:id>',views.delete_sem,name='delete_sem'),
    path('delete_course/<int:id>',views.delete_course,name='delete_course'),
    path('delete_time/<int:id>',views.delete_time,name='delete_time'),
    path('delete_room/<int:id>',views.delete_room,name='delete_room'),
]
