from django.shortcuts import render,redirect, get_object_or_404
from file_engine.models import File 
from file_engine.forms import FileForm, EditFileForm
from django.contrib import messages

# Create your views here.

def Home(request):

    return render(request, 'file_engine/home.html')




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
            return render(request, "file_engine/upload_file.html",{'form':form})
    else:
        form = FileForm(request.POST or None, request.FILES) 
        return render(request, "file_engine/upload_file.html",{'form':form})







def edit_file(request, id):
    file = get_object_or_404(File, id=id)
    form = EditFileForm(request.POST, request.FILES, instance=file)
    if request.method == "POST":
        form = EditFileForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            messages.info(request, "file updated successfully")
            return render(request,"file_engine/edit_file.html",{'form':form})
        else:
            return render(request, "file_engine/edit_file.html",{'form':form})
    else:
        return render(request, "file_engine/edit_file.html",{'form':form})



def delete_file(request, id):
    file = get_object_or_404(File, id=id)
    file.delete()
    messages.warning(request, "file deleted successfully ")
    return redirect("dashboard")