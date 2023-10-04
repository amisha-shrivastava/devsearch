from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):  #creates form based on the model
    class Meta:
        model = Project
        fields =  ['title', 'description', 'demo_link', 'source_link', 'tag'] #includes all editable fields '__all__'