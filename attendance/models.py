
from django.db import models
from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.contrib.auth.models import User
from datetime import datetime,date,time,timedelta
import datetime

#log models to storing all login logout
class log(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time=models.TimeField(null = True)
    logout_time=models.TimeField(null = True)
    date=models.DateField(null = True)
    status=models.CharField(max_length=10,null = True)
    working_hour=models.TimeField(null=True)

# attendance storing all filter login logout
class Attendance(models.Model):
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(null = True)
    logout_time = models.DateTimeField(null = True)

def user_store(sender,request,user,**kwargs):
    if user.is_staff==False:
        user_lis=[]
        a=log.objects.filter(user_id= user ,date=date.today())
        for i in a:
            user_lis.append(i.user_id)
        if user not in user_lis :
            users =User.objects.all()
            for user in users:
                if user.is_staff==False :
                    a=log.objects.create(user_id=user ,date=date.today(),status='Absent')
                    a.save()
    else:
        pass

user_logged_in.connect(user_store,sender=User)

#login signal
def user_login(sender,request,user,**kwargs):
   
    # print("user",(user.is_staf))
    
    if user.is_staff==False:
        user_lis=[]
        a=log.objects.filter(user_id= user ,date=date.today())
        for i in a:
            user_lis.append(i.user_id)
        # if user not in user_lis and time(22,3,30):
        #     users =User.objects.all()
        #     for user in users:
        #         log.objects.create(user_id=user ,date=date.today())
        if user in user_lis :
            z=log.objects.filter(user_id= user ,login_time=None).update(login_time= datetime.datetime.now().time(),status="Present")

        elif user in user_lis  :
            pass
            
        else:
            timings = log.objects.create(login_time = datetime.datetime.now().time(), user_id= user,date=date.today(),status="Present")
            timings.save()

user_logged_in.connect(user_login,sender=User)


#logout Signal
def logged_out(sender,request,user,**kwargs):
   
    if user_logged_out==None and user.is_staff==False:
        timing = log.objects.filter(user_id= user).first().date.today()
        a=log.objects.filter(user_id= user ,date=timing).create(logout_time= datetime.datetime.now().time())
        a.save()
    elif user.is_staff==False:
        timing = log.objects.filter(user_id= user).first().date.today()
        log.objects.filter(user_id= user ,date=timing).update(logout_time= datetime.datetime.now().time())
    else:
        pass
  
user_logged_out.connect(logged_out,sender=User)

def store_time(sender,request,user,**kwargs):
    if user.is_staff==False:

        Date = log.objects.filter(user_id= user).first().date.today()
        
        logs = log.objects.filter(user_id=user,date=Date)
    
        for Log in logs:

            enter=Log.login_time
            exit=Log.logout_time

            enter_delta = datetime.timedelta(hours=enter.hour, minutes=enter.minute, seconds=enter.second,microseconds=enter.microsecond)
            
            exit_delta = datetime.timedelta(hours=exit.hour, minutes=exit.minute, seconds=exit.second ,microseconds=exit.microsecond)
            difference_delta = exit_delta - enter_delta
            diff=log.objects.filter(user_id=user,date=Date).update(working_hour=str(difference_delta))
 
   
user_logged_out.connect(store_time,sender=User)

