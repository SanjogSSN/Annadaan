from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('blog-home')
        else:
            return view_func(request, *args, **kwargs)
        
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                if group == 'Volunteer':
                    return HttpResponse("<center style='font-size:32px;'>You do not have access to this page!<br>Only users registered as Donors can access this page</center>")
                else:
                    return HttpResponse("<center style='font-size:32px;'>You do not have access to this page!<br>Only users registered as Volunteers can access this page</center>")

        return wrapper_func
    return decorator