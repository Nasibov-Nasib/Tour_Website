from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Guide

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Guide
        fields = ['content']

# class PostAdmin(admin.ModelAdmin):
#     form = PostAdminForm

