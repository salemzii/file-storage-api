
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework import serializers as srlz

from .models import (file_uploader, 
                        image)
from .serializers import (file_uploader_serializer, 
                            image_serializer,)

from rest_framework.decorators import (api_view, 
                                    permission_classes, 
                                    action)
from rest_framework.parsers import (JSONParser, 
                                    MultiPartParser, 
                                    FormParser)
from rest_framework.decorators import parser_classes, permission_classes
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        IsAdminUser,
                                        AllowAny,
                            )
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework import status, viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from . import serializers
from django.core.exceptions import ImproperlyConfigured



def test_js(request):
    return render(request, "test.html")


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        'login': serializers.LoginSerializer,
        'register': serializers.UserRegisterSerializer,
        'password_change': serializers.PasswordChangeSerializer,
    }

    model = User.objects.all()
    queryset = User.objects.all()

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = request.data['username']
        password = request.data['password']
        data = {}
        user2 = User.objects.get(username=username)
        user = authenticate(username=username, password=password)
        user_token = Token.objects.get(user = user2)

        if user:
            data['auth_token'] = user_token.key
            data['username'] = username
            data['email'] = user2.email
            data['id'] = user2.id
            data['is_active'] = user2.is_active
            data['is_staff'] = user2.is_staff
        else:
            raise srlz.ValidationError("Invalid username/password. Please try again!")
        return Response(data=data, status=status.HTTP_200_OK)


    @action(methods=['POST', ], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data ={}
        validate_email = User.objects.filter(email=request.data['email'])
        if validate_email:
            data['invalid'] = "Email address already in use by another user!"
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create(username=request.data['username'], email=request.data['email'],
                    password = make_password(request.data['password']), first_name = request.data['first_name'], last_name = request.data['last_name']
                )
        token = Token.objects.create(user=user)
        data['id'] = user.id
        data['username'] = user.username
        data['authtoken'] = token.key
        data['email'] = user.email
        data['is_active'] = user.is_active
        data['is_staff'] = user.is_staff

        return Response(data=data, status=status.HTTP_201_CREATED)


    @action(methods=['POST', ], detail=False)
    def logout(self, request):
        logout(request)
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)


    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated, ])
    def password_change(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()





@api_view(["POST"])
@permission_classes((IsAuthenticated,))
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
@permission_classes((IsAuthenticated,))
def get_files(request):
    try:
        files = file_uploader.objects.all()
        serializer = file_uploader_serializer(files, many=True)
        return Response(serializer.data, status.HTTP_302_FOUND)
    except Exception as e:
        return Response(serializer.data, status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_file(request, fileId):
    try:
        file = file_uploader.objects.get(id=fileId)
        serializer = file_uploader_serializer(file, many=False)
        return Response(serializer.data, status.HTTP_302_FOUND)
    except Exception as e:
        return Response(serializer.data, status.HTTP_404_NOT_FOUND)



@api_view(["POST"])
@permission_classes((IsAuthenticated,))
@parser_classes([MultiPartParser])
def upload_image(request):
    serializer = image_serializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        print("Image SAVED!")
        return Response(serializer.data, status.HTTP_201_CREATED)

    else:
        print(serializer.errors)

    return Response(request.data, status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_images(request):
    try:
        files = image.objects.all()
        serializer = image_serializer(files, many=True)
        return Response(serializer.data, status.HTTP_302_FOUND)
    except Exception as e:
        return Response(serializer.data, status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_image(request, imageId):
    try:
        file = image.objects.get(id=imageId)
        serializer = image_serializer(file, many=False)
        return Response(serializer.data, status.HTTP_302_FOUND)
    except Exception as e:
        return Response(serializer.data, status.HTTP_404_NOT_FOUND)


