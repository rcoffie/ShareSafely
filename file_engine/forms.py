from django import forms 
from file_engine.models import File


class FileForm(forms.ModelForm):

    class Meta:
        model = File 
        fields = ('name','user','file','description')