from django.db import models
import graphene
from graphene_django import DjangoObjectType
from storageapp.models import file_uploader, image


class FileUploaderType(DjangoObjectType):
    class Meta: 
        model = file_uploader
        fields = ('id','name', 'file')


class ImageType(DjangoObjectType):
    class Meta:
        model = image
        fields = ('id', 'name', 'img')


class Query(graphene.ObjectType):
    files = graphene.List(FileUploaderType)
    images = graphene.List(ImageType)

    def resolve_files(root, info, **kwargs):
        # Querying a list
        return file_uploader.objects.all()

    def resolve_images(root, info, **kwargs):
        # Querying a list
        return image.objects.all()


schema = graphene.Schema(query=Query)