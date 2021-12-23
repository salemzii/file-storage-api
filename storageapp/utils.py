from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class AppTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return (text_type(user.is_active)+text_type(user.pk)+text_type(timestamp))


account_activation_token = AppTokenGenerator()



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




"""uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

domain = get_current_site(request).domain
link = reverse('activate', kwargs={'uidb64': uidb64, 'token': account_activation_token.make_token(user)})
activate_url = 'http://' + domain + link
email_subject = 'Activate your account'
email_body = 'Hello {0} thanks for signing up with us, please use this link to verify your account \n {1}'.format(
    user.username, activate_url)

email = send_mail(email_subject, email_body, 'Noreply@FX.com', [user.email], fail_silently= True)

data['link'] = link
data['activation_url'] = activate_url"""