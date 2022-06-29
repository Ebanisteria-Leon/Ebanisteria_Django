from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User

class CustomTokenObtainPairSerializers(TokenObtainPairSerializer):
    pass

class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'last_name', 'rolUser', 'image', 'codigoVerificacion',)

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'last_name', 'rolUser', 'image', 'codigoVerificacion')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UpdateUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'last_name', 'rolUser', 'image', 'codigoVerificacion')

    def update(self, instance, validated_data):
        if 'password' not in validated_data:
            update_user = super().update(instance, validated_data)
            update_user.save()
            return update_user
        
        else:
            update_user = super().update(instance, validated_data)
            update_user.set_password(validated_data['password'])
            update_user.save()
            return update_user

class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'last_name', 'rolUser', 'image', 'codigoVerificacion')

class PasswordSerializers(serializers.Serializer):
    password = serializers.CharField(max_length = 255, min_length = 6, write_only = True)
    password2 = serializers.CharField(max_length = 255, min_length = 6, write_only = True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                'password': 'Debe ingresar ambas contraseñas iguales'
            })

        return data
