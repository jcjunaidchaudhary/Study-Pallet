import os
from django.shortcuts import redirect, render
from django.http  import  HttpResponse
import random 
import numpy as np
from timetable.models import Course, Room, Sem, Time
from timetable.service import am_pm, convert_days, generate_docx
from django.core.files.storage import FileSystemStorage
from docx2pdf import convert
from datetime import date

# Create your views here.

def index(request):
    sem=Sem.objects.all()
    sem_idx=zip(sem, range(1, len(sem)+1))

    course=Course.objects.all()
    course_idx=zip(course, range(1, len(course)+1))

    time=Time.objects.all()
    time_idx=zip(time, range(1, len(time)+1))

    rooms=Room.objects.all()
    rooms_idx=zip(rooms, range(1, len(rooms)+1))

    time=[]
        # number_of_slots=int(input("Enter number of slots"))
    number_of_slots=Time.objects.all()
    # print(number_of_slots)
    for slot in number_of_slots:
        start=slot.start
        end=slot.end
        time.append(start+"-"+end+"  ")
        
    return render(request, 'index.html',{'sem':sem_idx, 'course':course_idx, 'time':time_idx,"rooms":rooms_idx,"time_slots":time})


def timetable(request):
        
    if request.method == 'POST':
        timetables = [] 
        sem=request.POST.get('sem','')
        department=request.POST.get('department','')
        sem=Sem.objects.filter(name=sem,department=department).first()
        k=request.POST.get('number')

        print(k)
        lst = []
        d = 0
        p = 0
        subnum=Course.objects.filter(sem_id=sem.id)

        lab=[]
        for sub in subnum:    
            if sub.is_lab==True:
                sub_code=sub.code+" G "+sub.uid
                if lab:
                    lab[0]=lab[0]+" / "+sub_code
                else:
                    lab.append(sub_code)
                
                continue

            sub_code=sub.code+" L "+sub.uid
            # f = int(input("enter frequency :"))
            f=sub.teaching_hour
            d = d + f
            for i in range(0, f):
                lst.append(sub_code)

        for i in range(3):
            lst.append(lab[0])                

        time=[]
        # number_of_slots=int(input("Enter number of slots"))
        number_of_slots=Time.objects.all()
        # print(number_of_slots)
        for slot in number_of_slots:
            start=slot.start
            end=slot.end
            time.append(start+"-"+end+"  ")

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
        
        for p in range(int(k)):
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
            timetables.append(matrix2)

            print("-----FE ", end="")
            print(p + 1, end="")
            print("------")
            print("TIME              MON  TUE  WED  THU  FRI")
            for i in range(R):
                print(time[i], end="")
                for j in range(C):
                    print(matrix2[i][j], end="  ")
                print()
            
        
        timetables_days=convert_days(timetables,time)
        # data={'timetables':timetables_days,'time_slotS':time}
        # return redirect(f'home?{data}')
        
        return render(request, 'index.html',{'timetables':timetables_days,'time_slotS':time})



def rooms(request):
    if request.method == 'POST':
        name=request.POST.get('name','')
        is_lab=request.POST.get('Check1')
        if is_lab=='on':
            is_lab=True
        else:
            is_lab=False
        rooms=Room(name=name, is_lab=is_lab)
        rooms.save()
    return redirect('home')


def course(request):
    if request.method == 'POST':
        code=request.POST.get('code','')
        name=request.POST.get('course','')
        teaching_hour=request.POST.get('teaching_hour','')
        is_lab=request.POST.get('Check1')
        if is_lab=='on':
            is_lab=True
        else:
            is_lab=False

        uid=request.POST.get('uid','')
        faculty=request.POST.get('faculty','')
        sem=request.POST.get('sem','')
        department=request.POST.get('department','')
        sem=Sem.objects.get(name=sem,department=department)
        course=Course(code=code,name=name,teaching_hour=teaching_hour,is_lab=is_lab,uid=uid,faculty=faculty,sem_id=sem.id)
        course.save()

    return redirect('home')

def sem(request):
    if request.method == 'POST':
        name=request.POST.get('name','')
        department=request.POST.get('department','')
        sem=Sem(name=name,department=department)
        sem.save()
    
    sem=Sem.objects.all()
    return redirect('home')
 
def time(request):
    if request.method == 'POST':
       
        start=request.POST.get('start','')
        start=am_pm(start)

        end=request.POST.get('end','')
        end=am_pm(end)
        time=Time(start=start,end=end)
        time.save()
    return redirect('home')

def timetable_docx(request):

    # data1=request.POST.get('timetable')
    # print(">>>>>>>>>>>>",data1)
    # sem=request.POST.get('sem')

    timetable=[{'time': '9.00am-10.00am  ', 'M': 'BC g VB / CC g ZM', 'T': '--', 'W': 'CCS L ZM', 'Th': '--', 'F': '--'}, {'time': '10.00am-11.00am  ', 'M': 'BDLT L VB', 'T': 'BDLT L VB', 'W': 'EM L AW', 'Th': '--', 'F': 'BC g VB / CC g ZM'}, {'time': '11.00am-12.00am', 'M': 'BDA L AS', 'T': 'BC g VB / CC g ZM', 
    'W': '--', 'Th': 'BDA L AS', 'F': 'BDA L AS'}, {'time': '12.00am-1.00am  ', 'M': '--', 'T': '--', 'W': '--', 'Th': '--', 'F': '--'}, {'time': '2.00am-3.00am  ', 'M': '--', 'T': 'EM L AW', 'W': '--', 'Th': 'CCS L ZM', 'F': 'CCS L ZM'}, {'time': '3.00am-4.00am  ', 'M': 'EM L AW', 'T': 'CCS L ZM', 'W': 'BDLT L VB', 'Th': 'EM L AW', 'F': '--'}]

    data={}
    # data={"department":"Information Technology","rooms":"208/306","semester":"VIII","date":"12-7-23"}
    
    sem=Sem.objects.get(name='VIII')
    current_date = date.today()
    rooms=Room.objects.filter(is_lab=False)

    data["department"]=sem.department
    data["semester"]=sem.name
    data["date"]=current_date.strftime("%d-%m-%Y")
    data["rooms"]=rooms[0].name+"/"+rooms[1].name
   
    generate_docx(timetable,data)

    docx=f"{data.get('semester')}.docx"

    fs = FileSystemStorage()
    filename = str(docx)
    with fs.open(filename) as docx:
        response = HttpResponse(docx, content_type='application/docx')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename) 
        # messages.success(request,"{} Resume Download Successfully!".format(user))
        return response

def timetable_pdf(request):
    timetable=[{'time': '9.00am-10.00am  ', 'M': 'BC g VB / CC g ZM', 'T': '--', 'W': 'CCS L ZM', 'Th': '--', 'F': '--'}, {'time': '10.00am-11.00am  ', 'M': 'BDLT L VB', 'T': 'BDLT L VB', 'W': 'EM L AW', 'Th': '--', 'F': 'BC g VB / CC g ZM'}, {'time': '11.00am-12.00am', 'M': 'BDA L AS', 'T': 'BC g VB / CC g ZM', 
    'W': '--', 'Th': 'BDA L AS', 'F': 'BDA L AS'}, {'time': '12.00am-1.00am  ', 'M': '--', 'T': '--', 'W': '--', 'Th': '--', 'F': '--'}, {'time': '2.00am-3.00am  ', 'M': '--', 'T': 'EM L AW', 'W': '--', 'Th': 'CCS L ZM', 'F': 'CCS L ZM'}, {'time': '3.00am-4.00am  ', 'M': 'EM L AW', 'T': 'CCS L ZM', 'W': 'BDLT L VB', 'Th': 'EM L AW', 'F': '--'}]

    # data={"department":"Information Technology","rooms":"208/306","semester":"VII","date":"12-7-23"}

    data={}
    
    sem=Sem.objects.get(name='VIII')
    current_date = date.today()
    rooms=Room.objects.filter(is_lab=False)

    data["department"]=sem.department
    data["semester"]=sem.name
    data["date"]=current_date.strftime("%d-%m-%Y")
    data["rooms"]=rooms[0].name+"/"+rooms[1].name

    generate_docx(timetable,data)

    convert(f"media/{data.get('semester')}.docx")

    fs = FileSystemStorage()
    filename = str(f"{data.get('semester')}.pdf")
    with fs.open(filename) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename) 
        
        return response

    

def delete_course(request,id):
    course=Course.objects.get(id=id)
    course.delete()
    return redirect('home')

def delete_room(request,id):
    del_room=Room.objects.get(id=id)
    del_room.delete()
    return redirect('home')

def delete_sem(request,id):
    del_room=Sem.objects.get(id=id)
    del_room.delete()
    return redirect('home')

def delete_time_slot(request,id):
    del_room=Time.objects.get(id=id)
    del_room.delete()
    return redirect('home')
    