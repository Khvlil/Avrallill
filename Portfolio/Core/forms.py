from django.forms import ModelForm, Textarea
from .models import *
from django import forms
from django.core import validators



class PostForm(ModelForm):
    class Meta:
        models = Post
        fields = "__all__"
        widgets = {
            "project_overview": Textarea(),
            "research_and_inspiration": Textarea(),
            "problem_statement": Textarea(),
            "concept_and_design_principles": Textarea(),
            "challenges_and_solutions": Textarea(),
            "conclusion_and_next_steps": Textarea(),
        }


class DesignForm(ModelForm):
    class Meta:
        model = Design
        fields = "__all__"

    def clean_image(self):
        data = self.cleaned_data["image"]
        # Get the original file name
        original_name = data.name

        print(original_name)

        return data


class ContactForm(ModelForm):
    email = forms.EmailField(max_length=254)
    subject = forms.CharField(required=True)

    class Meta:
        model = Contact
        fields = '__all__'
            
        
