from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as user_login, logout
from django.contrib import messages
from blog.models import *
from blog.decorators import *
import time

def home(request):
    context = {
        'fbs': Food_Bank.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def contact_us(request):
    return render(request, 'blog/feedback.html')

def mission(request):
    return render(request, 'blog/our_mission.html')

@unauthenticated_user
def signup(request):
    return render(request, 'blog/Volunteer_SignUp.html')

def food_bank(request):
    return render(request, 'blog/food_bank.html')
    
@login_required
@allowed_users(allowed_roles=['Donor'])
def req(request):
    return render(request, 'blog/request.html')

@unauthenticated_user
def login(request):
    return render(request, 'blog/login.html')

@unauthenticated_user
def loggedin(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        psw = request.POST.get('pass')

        user = authenticate(username= uname, password= psw)
        if user is not None:
            user_login(request, user)
            messages.success(request, f"Logged in successfully")
            return redirect('blog-home')
        else:
            messages.error(request, f"Your username and password didn't match. Try again!!")
            return render(request, 'blog/login.html')
    return render(request, 'errors/404.html')

def loggedout(request):
    logout(request)
    return redirect('blog-home')

def register(request):
    print(request.POST)
    psw = request.POST.get('pass')
    email = request.POST.get('email')
    name = request.POST.get('fname')
    if request.method == 'POST':
        if User.objects.filter(username=email).exists():
            messages.error(request, f'Email id is already registered! Try diffrent Email id')
            return redirect('blog-volunteer_signup')
        else:
            user = User.objects.create_user(
                first_name= name,username=email, password=psw, email= email
            )
        
        p = Profile()
        p.address = request.POST.get('address')
        p.user = user
        p.phone = request.POST.get('num')
        pt = request.POST.get('radio')
        p.ptype = pt
        
        group = Group.objects.get(name= pt)
        user.groups.add(group)

        if (pt =="Volunteer"):
            user.is_superuser = '1'
        
        if (pt =="Donor"):
            user.is_staff = '1'

        user.save()
        p.save()
        messages.success(request, f"You are registered successfully")
        return redirect('login/')
    else:
        return render(request, 'errors/404.html')

def foodbank(request):
    print(request.POST)
    if request.method == 'POST':
        fb = Food_Bank()
        fb.name = request.POST.get('fname')
        fb.phone = request.POST.get('num')
        fb.location = request.POST.get('loc')
        fb.incharge = request.POST.get('iname')
        fb.save()
        messages.success(request, "Food Bank is registered successfully")
        return redirect('blog-home')
    else:
        return render(request, 'errors/404.html')

def requested(request):
    print(request.POST)
    if request.method == 'POST':
        s = Status()
        s.description = "Requested"
        s.save()
        n = request.POST.get('fname')
        
        rq = Request()
        rq.food_item = request.POST.get('fi')
        rq.quantity = request.POST.get('qty')
        rq.location = request.POST.get('loc')
        rq.phone = request.POST.get('num')

        rq.did = Profile.objects.get(user = User.objects.get(first_name__iexact= n))
        rq.sid = Status.objects.last()
        rq.save()
        messages.success(request, "Your donation request has been sent")

        return redirect('blog-home')
    else:
        return render(request, 'errors/404.html')

@login_required
def check_status(request):
    return render(request, 'blog/Status.html')

def status(request):
    print(request.POST)
    if request.method == 'POST':
        r = request.POST.get('rno')
        context = {
            'rqs' : Request.objects.filter(id= r),
        }

        return render(request, 'blog/status.html', context)
    else:
        return render(request, 'errors/404.html')

@login_required
@allowed_users(allowed_roles=['Volunteer'])
def requestlist(request):       
    context = {
        'rqs' :  Request.objects.all()
    }
    return render(request, 'blog/request_list.html', context)

@login_required
@allowed_users(allowed_roles=['Volunteer'])
def volunteer_report(request):
    return render(request, 'blog/volunteer_report.html')

def volreport(request):
    print(request.POST)
    if request.method == 'POST':
        v = Reports()
        n = request.POST.get('vname')
        r = request.POST.get('rid')
        s = Status.objects.get(id= (Request.objects.values_list('sid', flat=True).get(id= r)))
        
        v.vid = Profile.objects.get(user = User.objects.get(first_name__iexact= n))
        v.rid = Request.objects.get(id= r)
        v.location = request.POST.get('location')
        v.human = request.POST.get('hum')
        v.animal = request.POST.get('ani')
        
        v.save()

        s.description = "Donated"
        s.save()
        messages.success(request, "Report has been generated successfully")

        return redirect('blog-home')
    else:
        return render(request, 'errors/404.html')

@login_required
@allowed_users(allowed_roles=['Volunteer'])
def onsite(request):
    return render(request, 'blog/onsite_processing.html')

def os_processing(request):
    print(request.POST)
    if request.method == 'POST':
        o = Onsite_Processing()
        n = request.POST.get('vname')
        r = request.POST.get('rid')
        s = Status.objects.get(id= (Request.objects.values_list('sid', flat=True).get(id= r)))
        
        o.vid = Profile.objects.get(user = User.objects.get(first_name__iexact= n))
        o.rid = Request.objects.get(id= r)
        o.smell = request.POST.get('sm')
        o.visual = request.POST.get('vis')
        o.result = request.POST.get('res')
        
        o.save()

        s.description = "Collected"
        s.save()
        messages.success(request, "Onsite Processing data is registered")

        return redirect('blog-home')
    else:
        return render(request, 'errors/404.html')

@login_required
@allowed_users(allowed_roles=['Volunteer'])
def donation(request):
    return render(request, 'blog/donation_process.html')

def don_process(request):
    print(request.POST)
    if request.method == 'POST':
        d = Donation_Process()
        r = request.POST.get('rid')
        s = Request.objects.values_list('sid', flat=True).get(id=r)
        st = Status.objects.get(id= s)

        d.sid = Status.objects.get(id= s)
        d.oid = Onsite_Processing.objects.get(rid= r)
        d.location = request.POST.get('location')
        d.dtype = request.POST.get('radio')

        if d.dtype == "food_bank":
            st.description = "Donated"
            st.save()
        
        d.save()
        messages.success(request, "Donation Process data is registered")

        return redirect('blog-home')
    else:
        return render(request, 'errors/404.html')

def vrs(request):
    context = {
        'c' : 0
    }
    return render(request, 'blog/vreport.html', context)

def vr(request):
    print(request.POST)
    if request.method == 'POST':
        v = request.POST.get('vno')
        r = request.POST.get('rno')
        context = {
            'vrs' : Reports.objects.filter(vid= v).all(),
            'c' : Reports.objects.filter(vid= v).count,
            'n' : Reports.objects.filter(rid= r).count,
            'r' : Request.objects.get(id=r)
        }
        return render(request, 'blog/vreport.html', context)
    else:
        return render(request, 'errors/404.html')

@login_required
def profile(request):
    context = {
        'pros': Profile.objects.filter(user= request.user)
    }
    return render(request, 'blog/profile.html', context)

def accept(request):
    print(request.POST)
    if request.method == 'POST':
        r = request.POST.get('rid')
        s = Status.objects.get(id= (Request.objects.values_list('sid', flat=True).get(id= r)))
    
        s.description = "Accepted"
        s.save()

        context = {
        'rqs' :  Request.objects.all()
        }
        return render(request, 'blog/request_list.html', context)
    else:
        return render(request, 'errors/404.html')

def change_password(request):
    return render(request, 'blog/change_password.html')    

def changed_password(request):
    print(request.POST)
    if request.method == 'POST':
        p = request.POST.get('pass')
        r = request.POST.get('rpass')
        uname= request.user.username

        if(p == r):
            u = User.objects.get(id= request.user.id)
            u.set_password(p)
            u.save()

            user = authenticate(username= uname, password= p)
            user_login(request, user)

            messages.success(request, f"Password Changed Successfully")
            return redirect('blog-profile')
        else:
            messages.error(request, f"Password doesn't match, Try again !!")
            return render(request, 'blog/change_password.html')
    else:
        return render(request, 'errors/404.html')
