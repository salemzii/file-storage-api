from os import name
from django.db import models
import graphene
from graphene_django import DjangoObjectType
from storageapp.models import file_uploader, image
from django.contrib.auth.models import User


class FileUploaderType(DjangoObjectType):
    class Meta: 
        model = file_uploader
        fields = ('id','name', 'file', 'date')


class ImageType(DjangoObjectType):
    class Meta:
        model = image
        fields = ('id', 'name', 'img', 'date')


class Query(graphene.ObjectType):
    files = graphene.List(FileUploaderType)
    images = graphene.List(ImageType)
    file = graphene.Field(FileUploaderType, id=graphene.UUID())
    image = graphene.Field(ImageType, id = graphene.UUID())


    def resolve_files(root, info, **kwargs):
        return file_uploader.objects.all()

    def resolve_images(root, info, **kwargs):
        return image.objects.all()

    def resolve_file(root, info, id, **kwargs):
        return file_uploader.objects.get(id=id)

    def resolve_image(root, info, id, **kwargs):
        return image.objects.get(id=id)


class ImageMutation(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)

    img = graphene.Field(ImageType)

    @classmethod
    def mutate(cls, root, Info, name):
        imgg = image(name=name)
        imgg.save()
        return ImageMutation(img=imgg)


class Mutation(graphene.ObjectType):
    update_image = ImageMutation.Field()
    

schema = graphene.Schema(query=Query, mutation=Mutation)