from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from file_engine. models import File
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 

# Create your views here.
@login_required(login_url="login")
def dashboard(request):
    user = request.user 
    files = File.objects.filter(user=user)
    context = {'files':files}

    return render(request, 'user_engine/dashboard.html',context)

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, (f"welcome {username}"))
                return redirect("dashboard")
            else:
                messages.warning("invalid username or password")
        else:
            messages.warning(request, "invalid username or password")
    form = AuthenticationForm()
    return render(request, "user_engine/login_request.html", {"form": form})