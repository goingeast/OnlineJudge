from django.contrib import admin
from .models  import Problem
from django import forms
from django.forms import TextInput, Textarea

class ProblemForm( forms.ModelForm ):
    description_text = forms.CharField( widget = forms.Textarea)
    test_cases = forms.CharField( widget = forms.Textarea)
    class Meta:
        model = Problem
        fields = '__all__'

class ProblemAdmin(admin.ModelAdmin):
    form = ProblemForm

admin.site.register(Problem, ProblemAdmin)
# Register your models here.
