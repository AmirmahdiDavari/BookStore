from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from django.apps import apps as django_apps
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken, TokenError
from rest_framework_simplejwt.settings import api_settings
from User.models import User

from rest_framework import authentication
from rest_framework import exceptions

def response(message, status, code, data=[]):
    message, code, status = "", 205, False
    return Response({"message": message, "data": data, "code": code, "status": status})

#
# class JwtAuth(JWTAuthentication):
#
#
#     def get_user(self, validated_token):
#         try:
#             user_id = validated_token[api_settings.USER_ID_CLAIM]
#             return user_id
#
#         except KeyError:
#             raise InvalidToken(_("Token contained no recognizable user identification"))
#
#
# def check_token(request):
#     JWT_authenticator = JwtAuth()
#     response = JWT_authenticator.get_user(request)
#     print (response)
#     if response is not None:
#         user, token = response
#         return user
#     else:
#         return False
class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('HTTP_X_USERNAME')
        print(username)
        if not username:
            print("توکن ارسال نشده است ")
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            print("توکن اشتباه است یا کاربر وجود ندارد  ")

            raise exceptions.AuthenticationFailed('No such user')
        print(" با موفقیت وارد شدید  ")

        return (user, None)

def check_token(request):
    authenticator = ExampleAuthentication()
    response=authenticator.authenticate(request)
    print(response)
    if response is not None:
        user = response
        return user
    else:
        return False