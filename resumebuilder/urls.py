from django.urls import path
from resumebuilder import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.viewprofile,name='viewprofile'),
    path('personalinfo/',views.personalinfo,name='personalinfo'),
    path('updatepersonalinfo/',views.updatepersonalinfo,name='editpersonalinfo'),
    path('workexperience/',views.workexperience,name='workexperience'),   
    path('updateworkexperience/<int:id>',views.updateworkexperience,name='updateworkexperience'),   
    path('education/',views.education,name='education'),
    path('updateeducation/<int:id>',views.updateeducation,name='updateeducation'),
    path('project/',views.project,name='project'),
    path('updateproject/<int:id>',views.updateproject,name='updateproject'),
    path('additionalinfo/',views.additionalinformation,name='additionalinfo'),
    path('updateadditionalinfo/<int:id>',views.updateadditionalinformation,name='updateadditionalinfo'),
    path('socialprofile/',views.socialprofile,name='socialprofile'),
    path('updatesocialprofile/<int:id>',views.updatesocialprofile,name='updatesocialprofile'),
    path('deleted/<int:id>',views.deleted,name='deleted'),
    path('destroy/<int:id>',views.destroy,name='destroy'),
    path('destruction/<int:id>',views.destruction,name='destruction'),
    path('destructor/<int:id>',views.destructor,name='destructor'),
    path('erase/<int:id>',views.erase,name='destructor'),
    path('generate/',views.Resume,name='resume'),
    path('download/',views.downloaddocx,name='download'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

