from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        
        user = authenticate(username = username, password = password)
        if user is not None :
            login(request, user)
            return redirect('dashboard')
        
        else:
            messages.error(request, "Bad request")
            return redirect('/')
    return render(request, 'signin.html')