from django.shortcuts import render
from file_engine. models import File

# Create your views here.
def dashboard(request):
    user = request.user 
    files = File.objects.filter(user=user)
    context = {'files':files}

    return render(request, 'user_engine/dashboard.html',context)