from django.shortcuts import render

# Create your views here.

def Home(request):

    return render(request, 'file_engine/home.html')