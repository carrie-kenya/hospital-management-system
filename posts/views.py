from django.shortcuts import render, HttpResponseRedirect
from .models import Patient
from django.contrib.auth import logout

# Create your views here.
def index(request):
    title = 'Home'
    return render(request, 'index.html', {title:title})


def patients(request):
    title = 'Patients'
    patients = Patient.objects.all()
    print(patients)
    return render(request, 'patients.html', {'title':title, 'patients':patients})    


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('Home')