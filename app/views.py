from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as lin ,logout as logo
from django.contrib.auth.decorators import login_required
from .forms import My_Form
from .models import My_Model

# Create your views here.

def register(request):
    if request.method=='POST':
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        if password != password2:
            return HttpResponse('password1 and password2 are not equal')
        else:
            saver = User.objects.create_user(username=name, password=password)

            # if User.objects.filter(username=name).exist():
                # return HttpResponse('the name that you are trying to write already exists')

            saver.save()

        return redirect('login')
    return render(request,'register.html')






def login(request):
    if request.method=='POST':
        name = request.POST.get('uname')
        password = request.POST.get('password')
        usee  = authenticate(request,username=name,password=password)
        print(usee)
        if usee is not None:
            lin(request,usee)
            return redirect('add')
        else:
            return redirect('register')





    return render(request,'login.html')




@login_required
def home(request):
    return render(request,'home.html')


def send(request):
    return render(request,'logout.html')



def logout(request):
    logo(request)
    return redirect('send')


# def add(request):


def add(request):
    if request.method=='POST':
        fm = My_Form(request.POST)
        if fm.is_valid():
            fm.save()
            fm = My_Form()
    else:
        fm = My_Form()
    sm = My_Model.objects.all()
    return render(request,'add.html',{'form':fm,'stu':sm})



def delete(request,id):
    if request.method=='POST':
        dl = My_Model.objects.get(pk=id)
        dl.delete()
    else:
        dl = My_Form(request.POST)
    return redirect('add')




def update(request,id):
    if request.method=='POST':
        sm = My_Model.objects.get(pk=id)
        fm = My_Form(request.POST,instance=sm)
        if fm.is_valid():
            fm.save()
            fm = My_Form()
    else:
        sm = My_Model.objects.get(pk=id)
        fm = My_Form(instance=sm)
    return render(request,'update.html',{'form':fm})    
