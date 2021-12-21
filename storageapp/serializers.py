from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import file_uploader


class file_uploader_serializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = file_uploader
        fields = ['name', 'file']

