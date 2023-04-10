from django.urls import path, include
from attendance import views

urlpatterns = [

   path('',views.showing_users,name='admin-sinterface'),
   path('user/<str:id>/',views.user_Attendance,name='user-week'),
   path('excel/<str:id>/',views.Excel_store,name='excel'),
   path('all/',views.All_Attendance,name='All-Attendance'),
   path('search/',views.search,name='search'),
   

]
