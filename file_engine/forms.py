from django import forms 
from file_engine.models import File


class FileForm(forms.ModelForm):

    class Meta:
        model = File 
        fields = ('name','file','description')


class EditFileForm(forms.ModelForm):

    class Meta:
        model = File 
        fields = ('file',)
