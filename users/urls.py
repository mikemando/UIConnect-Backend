from django.urls import path, include
from .views import VendorRegistrationView

urlpatterns = [
    path('register/', VendorRegistrationView.as_view(), name='register'),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]