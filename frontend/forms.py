from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.forms import fields
from storageapp.models import file_uploader, image


class file_Upload_form(forms.ModelForm):
    class Meta:
        model = file_uploader
        fields = ['name', 'file']


class image_Upload_form(forms.ModelForm):
    class Meta:
        model = image
        fields = ['name', 'img']