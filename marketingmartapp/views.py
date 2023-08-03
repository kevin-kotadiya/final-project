from django.shortcuts import render,redirect
from .form import signupform,updateprofile,noteform,feedbackform
from django.contrib import messages
from .models import user
from django.contrib.auth import logout
from django.core.mail import send_mail

# Create your views here.

def index(request):
    user = request.session.get('user')
     
    return render(request,'index.html',{'user':user})

def login(request):
    if request.method == "POST":
        uname = request.POST['username']
        password = request.POST['password']

        u = user.objects.filter(uname=uname,password=password)
        if u:
            userid = user.objects.get(uname=uname)
            request.session['user'] = uname
            request.session['userid'] = userid.id
            return redirect('/')
        else:
            print('check.............................................')
            messages.error(request,'Please Enter valid username or password')
            return redirect('login')   
           
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        # username = ''
        user1 = signupform(request.POST)
        if user1.is_valid():
            unm = user1.cleaned_data.get('uname')
            try:
                user.objects.get(uname = unm)
                messages.error(request,'User Already exist!!')
                return redirect('signup')
            except user.DoesNotExist:
                messages.success(request,'Signup succesfull Now you can login')
                user1.save()
                return redirect('login')
        else:
            messages.error(request,'Something went wrong! Please try again')
            return redirect('signup')
    return render(request,'signup.html')

def profile(request):
    user1 = request.session.get('user')
    userid = request.session.get('userid')
    uid = user.objects.get(id=userid)
    if request.method == 'POST':
        updprofile = updateprofile(request.POST,instance=uid)
        if updprofile.is_valid():
            updprofile.save()
            messages.success(request,'Profile upadte sucessfully')
            return redirect('profile')
        else:
            messages.error(request,updprofile.errors)

    uid = user.objects.get(id=userid)
    return render(request,'profile.html',{'user':user1,'uid':uid})

def lgout(request):
    logout(request)
    return redirect('/')

def notes(request):
    if request.method == 'POST':
        notes = noteform(request.POST,request.FILES)
        if notes.is_valid():
            notes.save()
            messages.success(request,'note uploaded successfully')
        else:
            print(notes.errors)
            messages.error(request,'something went wrong please try again!!')
    user1 = request.session.get('user')       
    return render(request,'notes.html',{'user':user1})

def about(request):
    user1 = request.session.get('user')
    return render(request,'about.html',{'user':user1})

def contact(request):
    user1 = request.session.get('user')

    if request.method == 'POST':
        feddback = feedbackform(request.POST)
        if feddback.is_valid():
            feddback.save()
            sub = 'Thank You!!'
            msg = 'Thank For feed back '
            from_id=''
            to_id = [request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)
            # msg = messages.success(request,'Feedback send seccessfully.')
            return redirect('contact')
        else:
            print(feddback.errors)

    return render(request,'contact.html',{'user':user1})

