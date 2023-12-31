from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from file_engine.models import File

from user_engine.forms import SignUpForm


# Create your views here.
@login_required(login_url="login")
def dashboard(request):
    user = request.user
    files = File.objects.filter(user=user)
    context = {"files": files}

    return render(request, "user_engine/dashboard.html", context)


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


# def signup(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password1")
#             login(request, user)
#             messages.info(request, (f"welcome {username}"))
#             return redirect("dashboard")
#     else:
#         form = SignUpForm()
#         return render(request, "user_engine/signup.html", {"form":form})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.info(request, (f"welcome {username}"))
            return redirect("dashboard")
    else:
        form = SignUpForm()
    return render(request, "user_engine/signup.html", {"form": form})



def logout_view(request):
    logout(request)
    return redirect('home')
