from rest_framework import serializers
from .models import file_uploader, image
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import password_validation
from django.contrib.auth.models import BaseUserManager



            
class file_uploader_serializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = file_uploader
        fields = ['name', 'file']


class image_serializer(serializers.ModelSerializer):

    img = serializers.ImageField()
    class Meta:
        model = image
        fields = ['name', 'img']
        

class LoginSerializer(serializers.Serializer):
    
    username = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)



class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
         model = User
         fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'auth_token')
         read_only_fields = ('id', 'is_active', 'is_staff')
    
    def get_auth_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key


class EmptySerializer(serializers.Serializer):
    pass




class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'email', 'password', 'first_name', 'last_name')

    def validate_email(self, value):
        print(value)
        try:
            user = User.objects.get(email=value)
            if user:
                raise serializers.ValidationError("Email is already taken")
        except Exception as e:
            return BaseUserManager.normalize_email(value)        

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value



class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password does not match')
        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value