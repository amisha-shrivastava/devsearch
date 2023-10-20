from django.forms import ModelForm, widgets
from django import forms
from .models import Project, Review


class ProjectForm(ModelForm):  #creates form based on the model
    class Meta:
        model = Project
        fields =  ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tag'] #includes all editable fields '__all__'
        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        }
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'input'})
        # self.fields['description'].widget.attrs.update({'class':'input', 'placeholder': 'Add Description'})
        
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']
        labels = {
            'value':'Place your vote.',
            'body': 'Add your comment.'
        }
        
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'input'})