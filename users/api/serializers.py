from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User

class CustomTokenObtainPairSerializers(TokenObtainPairSerializer):
    pass

class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'last_name', 'rolUser', 'image')

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UpdateUserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'last_name', 'rolUser', 'image')

class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'last_name', 'rolUser', 'image')

class PasswordSerializers(serializers.Serializer):
    password = serializers.CharField(max_length = 255, min_length = 6, write_only = True)
    password2 = serializers.CharField(max_length = 255, min_length = 6, write_only = True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                'password': 'Debe ingresar ambas contraseñas iguales'
            })

        return data
