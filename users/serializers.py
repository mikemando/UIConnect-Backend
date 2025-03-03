from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

User = get_user_model()

class CustomUserCreateSerializer(BaseUserCreateSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'whatsapp_number', 'password')

    def validate_email(self, value):
        if not value.endswith("@stu.ui.edu.ng"):
            raise serializers.ValidationError("Only university emails (@stu.ui.edu.ng) are allowed.")
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'whatsapp_number')
