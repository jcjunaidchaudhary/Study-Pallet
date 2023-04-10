from django.shortcuts import render
from django.http  import  HttpResponse
import random 
import numpy as np

from timetable.models import Course, Sem, Time

# Create your views here.

def timetable(request):
    sem_id=1
    lst = []
    d = 0
    p = 0
    # subnum = int(input("Enter number of subjects: "))
    subnum=Course.objects.filter(sem_id=sem_id)

    # print(subnum)
    for sub in subnum:    
        
        # sub = input("enter subject :")
        sub_code=sub.code+" L "+sub.uid
        # f = int(input("enter frequency :"))
        f=sub.teaching_hour
        d = d + f
        for i in range(0, f):
            lst.append(sub_code)

    print("lst---------",lst) 

    time=[]
    # number_of_slots=int(input("Enter number of slots"))
    number_of_slots=Time.objects.all()
    # print(number_of_slots)
    for slot in number_of_slots:
        start=slot.start
        end=slot.end
        time.append(start+"-"+end+"  ")

    print(time,"123")


    R = len(time)
    C = 5

    total_slots=R*C

    if (d > total_slots):
        print("invalid input")
    else:
        for i in range(0, total_slots - d):
            ele = "--"
            lst.append(ele)

    # k = int(input("enter number of timetables"))
    for p in range(1):
        lst1 = []
        matrix = []
        m = []
        #time = ["9-10  ", "10-11 ", "11-12 ", "12-1  ", "2-3   ","3-4  "]
        for i in range(R):
            a = []
            for j in range(C):
                item = lst[0]
                a.append(item)
                lst.remove(item)
                lst1.append(item)
            matrix.append(a)
            m = np.array(matrix)
            matrix1 = m.T
            for e in range(5):
                random.shuffle(matrix1[e])
            m1 = np.array(matrix1)
            matrix2 = m1.T
        for m in range(total_slots):
            lst.append(lst1[m])
        
        print(matrix2)
        print("-----FE ", end="")
        print(p + 1, end="")
        print("------")
        print("TIME              MON  TUE  WED  THU  FRI")
        for i in range(R):
            print(time[i], end="")
            for j in range(C):
                print(matrix2[i][j], end="  ")
            print()
        return HttpResponse("success")
    
# def faculty(request):
#     # if request.method == 'POST':
#     uid = "VB"
#     name="Vikas Bloda"
#     teaching_hour=20
#     faculty=Faculty(uid=uid,name=name,teaching_hour=teaching_hour,subject_code_id=6)    
#     faculty.save()
#     return HttpResponse("success")

def rooms(request):
    print("hello")
    return "hello"
    if request.method == 'POST':
        return "Hello"

def course(request):
    # if request.method == 'POST':
    code="EM"
    name="Environments Management"
    teaching_hour=4
    is_lab=False
    uid="AW"
    faculty="Amay Waghe"
    # print(">>>>>>>>>>>>>>>>>>>",sem_id)
    course=Course(code=code,name=name,teaching_hour=teaching_hour,is_lab=is_lab,uid=uid,faculty=faculty,sem_id=1)
    course.save()
    return HttpResponse("success")

def sem(request):
    # if request.method == 'POST':
    name="Sem 8"
    sem=Sem(name=name)
    sem.save()
    return HttpResponse("Successfully") 
 
def time(request):
    start="3.00am"
    end="4.00am"
    time=Time(start=start,end=end)
    time.save()
    return HttpResponse("success")