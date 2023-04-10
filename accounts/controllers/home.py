from django.shortcuts import redirect, render

def start(request):
    return render(request, 'home.html')