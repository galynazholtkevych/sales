from rest_framework.serializers import Serializer
from rest_framework.serializers import CharField


class LoginSerializer(Serializer):
    username = CharField()
    password = CharField(style={'input_type': 'password'})
