from django.shortcuts import render
from . import forms,models
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
    return render(request, 'hospital/index.html')

def patient_view(request):
    return render(request,'hospital/patient.html')

def patient_signup(request):
    userForm=forms.PatientForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect('patientlogin')
    return render(request,'hospital/patient_signup.html',context=mydict)