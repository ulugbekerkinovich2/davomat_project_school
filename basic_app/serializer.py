from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from basic_app import models
from basic_app.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.CustomUser


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(style={'input_type': 'username'})
    password = serializers.CharField(style={'input_type': 'password'})


class UserSerializer1(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = 'id', 'username', 'password', 'is_superuser', 'is_staff'

    def is_numeric(string):
        return string.is_numeric()

    def create(self, validated_data):
        print(validated_data)
        if len(validated_data["username"]) < 5:
            raise serializers.ValidationError('Ism 5 ta belgidan kam bo\'lmasligi kerak')
        if len(validated_data["password"]) < 8:
            raise serializers.ValidationError('Parol 8 ta belgidan kam bo\'lmasligi kerak')
        return models.CustomUser.objects.create_user(**validated_data)

    # def validate(self, data):
    #     if len(data['username']) < 5:
    #         raise serializers.ValidationError('Ism 5 ta belgidan kam bo\'lmasligi kerak')
    #     return data
    #
    # def validate(self, data):
    #     if len(data['password']) < 8:
    #         raise serializers.ValidationError('Parol 8 ta belgidan kam bo\'lmasligi kerak')
    #     return data


class UserPasswordSerializer(ModelSerializer):
    username = serializers.CharField(style={'input_type': 'username'})
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password',
            "is_superuser",
            "is_staff"
        ]

        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"write_only": True},
        }

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Student
