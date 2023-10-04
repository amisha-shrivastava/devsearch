from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):  #creates form based on the model
    class Meta:
        model = Project
        fields = '__all__' #includes all editable fields