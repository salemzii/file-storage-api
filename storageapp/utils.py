from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import check_password


def get_and_authenticate_user(username, password):

    user = authenticate(username=username, password=password)
    if user:
        return user
    else:
        raise serializers.ValidationError("Invalid username/password. Please try again!")



def create_user_account(email, password, first_name="",
                        last_name="", **extra_fields):
    user = User.objects.create(
        email=email, password=password, first_name=first_name,
        last_name=last_name, **extra_fields)

    return user