from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from file_engine.forms import EditFileForm, FileForm
from file_engine.models import File

# Create your views here.


def Home(request):
    return render(request, "file_engine/home.html")


@login_required(login_url="login")
def upload_file(request):
    form = FileForm(request.POST or None, request.FILES)
    if request.method == "POST" or None:
        form = FileForm(request.POST or None, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            # print(form)
            # print("valid form")
            file.user = request.user
            form.save()
            messages.success(request, "file uploaded successfully")
            return redirect("dashboard")
        else:
            # print(form)
            # print("invalid form")
            # print(form.errors)
            return render(request, "file_engine/upload_file.html", {"form": form})
    else:
        form = FileForm(request.POST or None, request.FILES)
        return render(request, "file_engine/upload_file.html", {"form": form})

@login_required(login_url="login")
def edit_file(request, id):
    file = get_object_or_404(File, id=id)
    print(file.user)
    if file.user == request.user:
        form = EditFileForm(request.POST, request.FILES, instance=file)
        if request.method == "POST":
            form = EditFileForm(request.POST, request.FILES, instance=file)
            if form.is_valid():
                form.save(commit=False)
                form.save()
                messages.info(request, "file updated successfully")
                return render(request, "file_engine/edit_file.html", {"form": form})
            else:
                return render(request, "file_engine/edit_file.html", {"form": form})
        else:
            return render(request, "file_engine/edit_file.html", {"form": form})
    else:
        return redirect('home')

@login_required(login_url="login")
def delete_file(request, id):
    file = get_object_or_404(File, id=id)
    if file.user == request.user:
        file.delete()
        messages.warning(request, "file deleted successfully ")
    else:
        return redirect('home')
    return redirect("dashboard")
