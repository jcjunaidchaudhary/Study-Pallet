from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout

def signout(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('/')