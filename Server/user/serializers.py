from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, Employer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'name', 'profile_picture', 'is_employer']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'name', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ['user', 'company_name', 'company_info']
