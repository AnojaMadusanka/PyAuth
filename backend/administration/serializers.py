from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'detail': 'data'
    }

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'first_name', 'last_name', 'is_active']