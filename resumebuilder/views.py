from django.shortcuts import render,redirect
from resumebuilder.models import PersonalInformation,WorkExperience,Educations,Projects,additionalinfo,Social_Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.http import HttpResponse
from resumebuilder.resumes import generateResume
from django.core.files.storage import FileSystemStorage



# Create your views here.
def personalinfo(request):
    if request.method=='POST':
        user=request.user
        name=request.POST.get('name','')    
        gender=request.POST.get('gender','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        marital_status=request.POST.get('marital_status','')
        date_of_birth=request.POST.get('date_of_birth','')
        profession=request.POST.get('profession','')
        objective=request.POST.get('objective','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        country=request.POST.get('country','')
        try:
            personalinfo=PersonalInformation(user=user,name=name,state=state,gender=gender,phone=phone,email=email,marital_status=marital_status,date_of_birth=date_of_birth,profession=profession,objective=objective,city=city,country=country)          
            personalinfo.save()
            messages.success(request,"{} Your Personal Information Save Successfully!".format(user))
            return redirect("viewprofile")
        except:
            pass
    messages.error(request,"{} Your Personal Information Already Exists!".format(user))
    return redirect("viewprofile")





def updatepersonalinfo(request):
    user=request.user
    personalinfo=PersonalInformation.objects.get(user_id=user)
    if request.method=='POST':
        name=request.POST.get('name','')
        gender=request.POST.get('gender','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        marital_status=request.POST.get('marital_status','')
        date_of_birth=request.POST.get('date_of_birth','')
        profession=request.POST.get('profession','')
        objective=request.POST.get('objective','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        country=request.POST.get('country','')
        try:
            personalinfo.name=name
            personalinfo.gender=gender
            personalinfo.phone=phone
            personalinfo.email=email
            personalinfo.marital_status=marital_status
            personalinfo.date_of_birth=date_of_birth
            personalinfo.profession=profession
            personalinfo.objective=objective
            personalinfo.city=city
            personalinfo.state=state
            personalinfo.country=country
            personalinfo.save() 
            messages.success(request,"{} Your Personal Information Update Successfully!".format(user))
            return redirect("viewprofile")
        except:
            pass
    messages.error(request,"{} Your Personal Information Not Update Successfully!".format(user))
    return redirect("viewprofile")
    




def workexperience(request):
    if request.method == 'POST':
        user=request.user
        company_name=request.POST.get('company_name','')
        location=request.POST.get('location','')
        joining_date=request.POST.get('jd','')
        end_date=request.POST.get('ed')
        if end_date == "":
            end_date="Present"
        designation=request.POST.get('designation','')
        working_on=request.POST.get('working_on','')
        try:
            obj=WorkExperience(user=user,company_name=company_name,location=location,joining_date=joining_date,end_date=end_date,designation=designation,working_on=working_on)
            obj.save()
            messages.success(request,"{} Your Work Experience Save Successfully!".format(user))
            return redirect("viewprofile")
        except:
            pass
    messages.error(request,"{} Please Fill Details Correctly".format(user))
    return redirect("viewprofile")



def updateworkexperience(request,id):
    user=request.user
    obj=WorkExperience.objects.get(id=id)
    if request.method == 'POST':
        company_name=request.POST.get('company_name','')
        location=request.POST.get('location','')
        joining_date=request.POST.get('jd','')
        end_date=request.POST.get('ed','')
        designation=request.POST.get('designation','')
        working_on=request.POST.get('working_on','')
        try:
            obj.company_name=company_name
            obj.location=location
            obj.joining_date=joining_date
            obj.end_date=end_date
            obj.designation=designation
            obj.working_on=working_on
            obj.save()
            messages.success(request,"{} Your WorkExperience Details Update Successfully".format(user))
            return redirect('viewprofile')    
        except:
            messages.error(request,'{} Your WorkExperience Details  Update Not Successfully'.format(user))
            return redirect('viewprofile')
    return redirect('viewprofile')
            
            

        

def education(request):
    if request.method=='POST': 
        user=request.user
        institute=request.POST.get('institute','')
        education=request.POST.get('education','')
        passingyear=request.POST.get('passing_year','')
        score=request.POST.get('score','')
        try:
            edu=Educations(user=user,institute=institute,education=education,passing_year=passingyear,score=score)          
            edu.save()
            messages.success(request,"{} Your Education Details Save Successfully!".format(user))
            return redirect("viewprofile")
        except:
            pass
    messages.error(request,"{} Please Fill Details Correctly!".format(user))
    return redirect("viewprofile")




def updateeducation(request,id):
    user=request.user
    obj=Educations.objects.get(id=id)
    if request.method=='POST': 
        institute=request.POST.get('institute','')
        education=request.POST.get('education','')
        passingyear=request.POST.get('passing_year','')
        score=request.POST.get('score','')
        try:
            obj.institute=institute
            obj.education=education
            obj.passing_year=passingyear
            obj.score=score
            obj.save()
            messages.success(request,"{} Your Education Details Update Successfully!".format(user))
            return redirect("viewprofile")
        except:
            pass
    messages.error(request,"{} Your Education Details Update Not Successfully!".format(user))
    return redirect("viewprofile")
        
        
        
        

def additionalinformation(request):
    if request.method == 'POST':
        user=request.user
        skill=request.POST.get('skill','')
        language=request.POST.get('language','')
        personal_wl=request.POST.get('personal_wl','')
        try:
            additional=additionalinfo(user=user,skill=skill,language=language,personal_wl=personal_wl)
            additional.save()
            messages.success(request,"{} Your Additional Information Save Successfully!".format(user))
            return redirect("viewprofile")
        except:
            pass
    messages.error(request,"{} Your Additional Information Already Exists!".format(user))
    return redirect("viewprofile")



def updateadditionalinformation(request,id):
    user=request.user
    obj=additionalinfo.objects.get(id=id)
    if request.method == 'POST':
        skill=request.POST.get('skill','')
        language=request.POST.get('language','')
        personal_wl=request.POST.get('personal_wl','')
        try:
            obj.skill=skill
            obj.language=language
            obj.personal_wl=personal_wl
            obj.save()
            messages.success(request,"{} Your Additional Information Update Successfully!".format(user))
            return redirect("viewprofile")
        except:
            pass
    messages.error(request,"{} Your Additional Information Update Not Successfully!".format(user))
    return redirect("viewprofile")



      
def project(request):
    if request.method=='POST':
        user=request.user
        title=request.POST.get('title','')
        description=request.POST.get('description','')
        try:
            obj=Projects(user=user,title=title,description=description)
            obj.save()
            messages.success(request,"{} Your Project Details Save Successfully!".format(user))
            return redirect("viewprofile")
        except:
            pass
    messages.error(request,"{} Please Fill Details Correctly!".format(user))
    return redirect("viewprofile")


def updateproject(request,id):
    user=request.user
    obj=Projects.objects.get(id=id)
    if request.method=='POST':
        title=request.POST.get('title','')
        description=request.POST.get('description','')
        try:
            obj.title=title
            obj.description=description
            obj.save()
            messages.success(request,"{} Your Project Details Update Successfully!".format(user))
            return redirect("viewprofile")
        except:
            pass
    messages.error(request,"{} Your Project Details Update Not Successfully!".format(user))
    return redirect("viewprofile")




def socialprofile(request):
    if request.method == 'POST':
        user=request.user
        social=request.POST.get('socialprofile','')
        link=request.POST.get('link','')
        try:
            obj=Social_Profile(user=user,social_profile=social,url=link)
            obj.save()
            messages.success(request,"{} Your {} Profile {} Save Successfully".format(user,social,link))
            return redirect('viewprofile')
        except:
            pass
    messages.error(request,"{} Your {} Profile {} Not Save Successfully".format(user,social,link))
    return redirect('viewprofile')


def updatesocialprofile(request,id):
    user=request.user
    obj=Social_Profile.objects.get(id=id)
    if request.method == 'POST':
        social=request.POST.get('socialprofile','')
        link=request.POST.get('link','')
        try:
            obj.social_profile=social
            obj.url=link
            obj.save()
            messages.success(request,"{} Your {} Profile {} Update Successfully".format(user,social,link))
            return redirect('viewprofile')
        except:
            pass
    messages.error(request,"{} Your {} Profile {} Update Not Successfully".format(user,social,link))
    return redirect('viewprofile')
        
        
        
@login_required
def viewprofile(request):
    try:
        user=request.user.id
        personalinformation=PersonalInformation.objects.get(user_id=user)
        workexperience=WorkExperience.objects.filter(user_id=user).order_by("-id")
        eduction=Educations.objects.filter(user_id=user).order_by("-id")
        project=Projects.objects.filter(user_id=user).order_by("-id")
        additional=additionalinfo.objects.filter(user_id=user).order_by("-id")
        social=Social_Profile.objects.filter(user_id=user).order_by("-id")
        return render(request,'resumebuilder/index.html',{'personal':personalinformation,'work':workexperience,'educ':eduction,'proj':project,'additi':additional,'social':social})
    except:
        return render(request,'resumebuilder/index.html')



def deleted(request,id):
    user=request.user
    wk=WorkExperience.objects.get(id=id)
    wk.delete()
    messages.success(request,"{} Your Work Experience Details Delete Successfully!".format(user))
    return redirect("viewprofile")




def destroy(request,id):
    user=request.user
    ed=Educations.objects.get(id=id)
    ed.delete()
    messages.success(request,"{} Your Education Details Delete Successfully!".format(user))
    return redirect("viewprofile")




def destruction(request,id):
    user=request.user
    pr=Projects.objects.get(id=id)
    pr.delete()
    messages.success(request,"{} Your Projects Details Delete Successfylly!".format(user))
    return redirect("viewprofile")




def destructor(request,id):
    user=request.user
    ad=additionalinfo.objects.get(id=id)
    ad.delete()
    messages.success(request,"{} Your Additional Information Details Delete Successfully!".format(user))
    return redirect("viewprofile")




def erase(request,id):
    user=request.user
    sp=Social_Profile.objects.get(id=id)
    sp.delete()
    messages.success(request,"{} Your Social Profile Delete Successfully!".format(user))
    return redirect("viewprofile")



def Resume(request):
    try:
        user=request.user
        pr=PersonalInformation.objects.get(user_id=user)
        wke=WorkExperience.objects.filter(user_id=user)
        ed=Educations.objects.filter(user_id=user)
        prj=Projects.objects.filter(user_id=user)
        add=additionalinfo.objects.get(user_id=user)
        so=Social_Profile.objects.filter(user_id=user) 
        generateResume(user=user,personal=pr,education=ed,experience=wke,projects=prj,social=so,add_Info=add)
        messages.success(request,"{} Your Resume has been generated now you can download".format(user))
        return redirect('viewprofile')
    except:
        messages.error(request,'{} Please Create Your Profile First'.format(user))
        return redirect('viewprofile')

def downloaddocx(request):   
    try:
        user=request.user
        pr=PersonalInformation.objects.get(user_id=user)
        docx=f"{pr.name}.docx"
        fs = FileSystemStorage()
        filename = str(docx)
        with fs.open(filename) as docx:
            response = HttpResponse(docx, content_type='application/docx')
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename) #user will be prompted with the browser’s open/save file
            #response['Content-Disposition'] = 'inline; filename="mypdf.pdf"' #user will be prompted display the PDF in the browser
            messages.success(request,"{} Resume Download Successfully!".format(user))
            return response
    except:
        messages.error(request,"{} Please Generate Resume".format(user))
        return redirect('viewprofile') 

  
