from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserCreateSerializer

class VendorRegistrationView(generics.CreateAPIView):
    '''
    - Handles registration for student vendors with a valid school email
    '''
    serializer_class = CustomUserCreateSerializer
    permission_classes = [permissions.AllowAny]
