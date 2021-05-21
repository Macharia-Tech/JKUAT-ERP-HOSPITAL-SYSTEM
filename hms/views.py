from django.shortcuts import render,redirect
from .models import DoctorDetail,PatientDetail,MedicienDetail
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate,login,logout



def Home(request):
    return render(request,"home.html")

#Doctor view ,delete and update
class Add_doctor(View):
    def get(self, request):
        return render(request,"adddoc.html")
    
    def post(self, request):
        name = request.POST["name"]
        code = request.POST["code"]
        mobile = request.POST["mobile"]
        location = request.POST["location"]
            
        if len(name)<3:
            messages.error(request,"Enter minimum 3 charcters in name field")
        elif len(code)<4 or code.isspace()==True:
            messages.error(request,"Enter minimum 4 charcters in Doctot code field, combination of numric and characters must!!")
        elif len(mobile)<10 or len(mobile)>10 or mobile.isdigit()!=True or mobile.isspace()==True: 
            messages.error(request,"Please enter minimum 10 numeric digits only and ensure there is no space in between!!")
        elif len(location)<3 or location.isalpha()!=True or location.isspace()==True:
            messages.error(request,"Enter minimum 3 charcters in location field and ensure that there is no space in between and no numeric value!!")
        else:
            try:
                DoctorDetail.objects.create(Name=name, Code=code, Mobile_No=mobile, Location=location)
                messages.success(request,"New Record Inserted Successfully!!")
                return redirect('view-doctor')
            except Exception:
                messages.error(request,"make sure Doctor Code is Unique Value!!")
                return render(request,'adddoc.html')
        return render(request,"adddoc.html")

class Update_doctor(View):
    def get(self,request,id):
        doctor = DoctorDetail.objects.get(id=id)
        return render(request,"edit_doc.html",{'doctor':doctor})
    
    def post(self,request,id):
        name = request.POST["name"]
        code = request.POST["code"]
        mobile = request.POST["mobile"]
        location = request.POST["location"]
        
        if len(name)<3:
           messages.error(request,"Enter minimum 3 charcters in name field")  
        elif len(mobile)<10 or len(mobile)>10 or mobile.isdigit()!=True or mobile.isspace()==True: 
            messages.error(request,"Please enter minimum 10 numeric valye in mobile field and ensure there is no space in between!!")
        elif len(location)<3 or location.isalpha()!=True or location.isspace()==True:
           messages.error(request,"Enter minimum 3 charcters in location field and ensure that there is no space in between and no numeric value!!")     
        else:
            try:
                doctor=DoctorDetail(id = id, Name=name, Code=code, Mobile_No=mobile, Location=location)
                messages.success(request,"Record Updated Successfully!!")
                doctor.save()
                return redirect('view-doctor')
            except Exception:
                messages.error(request,"Something went wrong")
        doctor = DoctorDetail.objects.get(id=id)
        return render(request,"edit_doc.html",{'doctor':doctor})

def delete_doctor(request,id):
    doctor =DoctorDetail.objects.get(id=id)
    doctor.delete()
    messages.success(request,"a record remove Successfully!!")
    return redirect("view-doctor")

def view_doctor(request):
    doctor = DoctorDetail.objects.all()
    return render(request,"view_doctor.html",{'doctor':doctor})

class Add_patient(View):
    def get(self, request): 
        return render(request,"add_patient.html")
    
    def post(self, request):
        name = request.POST["name"]
        mobile = request.POST["mobile"]
        location = request.POST["location"]
            
        if len(name)<3:
            messages.error(request,"Enter minimum 3 charcters in name field")
        elif len(mobile)<10 or len(mobile)>10 or mobile.isdigit()!=True or mobile.isspace()==True: 
            messages.error(request,"Please enter minimum 10 numeric digits only and ensure there is no space in between!!")
        elif len(location)<3 or location.isalpha()!=True or location.isspace()==True:
            messages.error(request,"Enter minimum 3 charcters in location field and ensure that there is no space in between and no numeric value!!")
        else:
            try:
                PatientDetail.objects.create(Name=name, Mobile_No=mobile, Location=location)
                messages.success(request,"New Record Inserted Successfully!!")
                return redirect('view-patient')
            except Exception:
                messages.error(request,"Something went wrong!!")
                return render(request,'add_patient.html')
        return render(request,"add_patient.html")

class Update_patient(View):
    def get(self,request,id):
        patient = PatientDetail.objects.get(id=id)
        return render(request,"edit_patient.html",{'patient':patient})
    
    def post(self,request,id):
        name = request.POST["name"]
        mobile = request.POST["mobile"]
        location = request.POST["location"]
        
        if len(name)<3:
           messages.error(request,"Enter minimum 3 charcters in name field")  
        elif len(mobile)<10 or len(mobile)>10 or mobile.isdigit()!=True or mobile.isspace()==True: 
            messages.error(request,"Please enter minimum 10 numeric valye in mobile field and ensure there is no space in between!!")
        elif len(location)<3 or location.isalpha()!=True or location.isspace()==True:
           messages.error(request,"Enter minimum 3 charcters in location field and ensure that there is no space in between and no numeric value!!")     
        else:
            try:
                doctor=DoctorDetail(id = id, Name=name, Mobile_No=mobile, Location=location)
                messages.success(request,"Record Updated Successfully!!")
                doctor.save()
                return redirect('view-patient')
            except Exception:
                messages.error(request,"Something went wrong")
        patient = PatientDetail.objects.get(id=id)
        return render(request,"edit_patient.html",{'patient':patient})

def delete_patient(request,id):
    patient =PatientDetail.objects.get(id=id)
    patient.delete()
    messages.success(request,"a record remove Successfully!!")
    return redirect("view-patient")

def view_patient(request):
    patient = PatientDetail.objects.all()
    return render(request,"view_patient.html",{'patient':patient})

class Add_medicine(View):
    def get(self, request):
        return render(request,"add_medicine.html")
    
    def post(self, request):
        name = request.POST["name"]
        code = request.POST["code"]
        cname = request.POST["cname"]
            
        if len(name)<3:
            messages.error(request,"Enter minimum 3 charcters in name field")
        elif len(code)<4 or code.isspace()==True:
            messages.error(request,"Enter minimum 4 charcters in Doctot code field, combination of numric and characters must!!")
        if len(cname)<3:
            messages.error(request,"Enter minimum 3 charcters in company name field")
        else:
            try:
                MedicienDetail.objects.create(Name=name, Code=code, Company_Name=cname)
                messages.success(request,"New Record Inserted Successfully!!")
                return redirect('view-medicine')
            except Exception:
                messages.error(request,"Something went wrong!!")
                return render(request,'add_medicine.html')
        return render(request,"add_medicine.html")

class Update_medicine(View):
    def get(self, request,id):
        medicine = MedicienDetail.objects.get(id=id)
        return render(request,"edit_medicine.html",{'medicine': medicine})
    
    def post(self, request,id):
        name = request.POST["name"]
        code = request.POST["code"]
        cname = request.POST["cname"]
            
        if len(name)<3:
            messages.error(request,"Enter minimum 3 charcters in name field")
        elif len(code)<4 or code.isspace()==True:
            messages.error(request,"Enter minimum 4 charcters in Doctot code field, combination of numric and characters must!!")
        if len(cname)<3:
            messages.error(request,"Enter minimum 3 charcters in company name field")
        else:
            try:
                medicine=MedicienDetail(id=id,Name=name, Code=code, Company_Name=cname)
                messages.success(request,"A Record updated successfully!!")
                medicine.save()
                return redirect('view-medicine')
            except Exception:
                messages.error(request,"Something went wrong!!")
                return render(request,'edit_medicine.html')
        medicine = MedicienDetail.objects.get(id=id)
        return render(request,"edit_medicine.html",{'medicine': medicine})

def delete_medicine(request,id):
    medicine = MedicienDetail.objects.get(id=id)
    medicine.delete()
    messages.success(request,"a record remove Successfully!!")
    return redirect("view-medicine")


def view_medicine(request):
    medicine = MedicienDetail.objects.all()
    return render(request,"view_med.html",{'medicine':medicine})

def log(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username,password=password)
            try:
                if user.is_staff:
                    login(request,user)
                    messages.success(request,"You Have logged In  Successfully!!")
                    return redirect("/")
            except Exception:
                messages.error(request,"Something went wrong!!")
                return redirect("log")
        return render(request,"login.html")
    else:
        messages.error(request,"You have already logged in")
        return redirect("/")

def log_out(request):
    if request.user.is_authenticated:
      logout(request)
      return redirect('log')
    else:
      messages.error(request,"You are not logged in")
      return redirect("/")
    