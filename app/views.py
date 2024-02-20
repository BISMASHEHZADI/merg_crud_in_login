from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as lin ,logout as logo
from django.contrib.auth.decorators import login_required

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
            return redirect('home')
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
        

    