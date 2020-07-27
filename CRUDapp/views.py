from django.shortcuts import render,HttpResponse,redirect
from .forms import UserForm
from .models import User

# Create your views here.

# This function Save and List or reterive data

def index(request):
    #return HttpResponse('<h1> Welcome Page </h1>')
    if request.method == 'POST':
        f=UserForm(request.POST)
        if f.is_valid():

            f.save()
            f=UserForm()
            #return HttpResponse('<h2>Success</h2>')
            return redirect('/')

    else:
        f=UserForm()
        stu=User.objects.all()
    return render(request,'index.html',{'form':f,'stud':stu})

# Update Operations

def update(request,id):
    if request.method == 'POST':
        u=User.objects.get(pk=id)
        f=UserForm(request.POST,instance=u)
        if f.is_valid():
            f.save()
    else:
        u=User.objects.get(pk=id)
        f=UserForm(instance=u) 

    return render(request,'update.html',{'form':f})

# Delete Operations

def deletestudent(request,id):
    if request.method == 'POST':
        f=User.objects.get(pk=id)
        f.delete()

        return redirect('/')
