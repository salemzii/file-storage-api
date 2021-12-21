from django.shortcuts import render
from rest_framework import serializers
from .models import file_uploader
from .serializers import file_uploader_serializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status



def test_js(request):
    return render(request, "test.html")



@api_view(["GET","POST"])
def upload_file(request):
    serializer = file_uploader_serializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        print("POST SAVED!")
        return Response(serializer.data, status.HTTP_201_CREATED)

    else:
        print(serializer.errors)
    return Response(request.data, status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_files(request):
    try:
        files = file_uploader.objects.all()
        serializer = file_uploader_serializer(files, many=True)
        return Response(serializer.data, status.HTTP_302_FOUND)
    except Exception as e:
        return Response(serializer.data, status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_file(request, fileId):
    try:
        file = file_uploader.objects.get(id=fileId)
        serializer = file_uploader_serializer(file, many=False)
        return Response(serializer.data, status.HTTP_302_FOUND)
    except Exception as e:
        return Response(serializer.data, status.HTTP_404_NOT_FOUND)



