from pickle import TRUE
from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from .forms import studentreg
from .models import user

# Create your views here.
def loginpage(request):
   

    return render(request,'djapp/login.html')


def add_show(request):
    if request.method=='POST':
        fm=studentreg(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=user(name=nm,email=em,password=pw)
            reg.save()
            fm=studentreg()
    
    else:
        fm=studentreg()
    stu=user.objects.all()
    return render(request,"djapp/add.html",{'form':fm,'stud':stu})

def update_data(request,id):
    if request.method=='POST':
        pi =user.objects.get(pk=id)
        fm=studentreg(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi =user.objects.get(pk=id)
        fm=studentreg(instance=pi)


    return render(request,"djapp/update.html",{'form':fm})

def delete(request,id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

    
