from django.shortcuts import render,redirect
from file_engine.models import File 
from file_engine.forms import FileForm

# Create your views here.

def Home(request):

    return render(request, 'file_engine/home.html')




def upload_file(request):
    if request.method == "POST" or None:
        form = FileForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            # print(form)
            # print("valid form")
            form.save()
            return render(request,"file_engine/upload_file.html",{'form':form})
        else:
            # print(form)
            # print("invalid form")
            # print(form.errors)
            return render(request, "file_engine/upload_file.html",{'form':form})
    else:
        return render(request, "file_engine/upload_file.html")