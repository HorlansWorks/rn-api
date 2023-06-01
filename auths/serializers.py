from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

User = User


class CreateUserSerializers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['uid', 'username', 'first_name', 'last_name',
                  'email', 'password',]

    def validate(self, attrs):
        registered_username = User.objects.filter(
            username=attrs['username']).exists()

        if registered_username:
            raise serializers.ValidationError(detail="user already exist")

        registered_email = User.objects.filter(
            username=attrs['email']).exists()

        if registered_email:
            raise serializers.ValidationError(detail="email already exist")

        return super().validate(attrs)

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],

        )
        user.set_password(validated_data['password'])

        user.save()
        return user


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ['uid', 'username', 'first_name',
                  'last_name', 'role', 'connects']


class UserJobStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStack
        fields = ['id', 'user_id', 'name']
