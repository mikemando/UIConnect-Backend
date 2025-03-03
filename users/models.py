from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.timezone import now


class CustomUserManager(BaseUserManager):
    '''
    - Validates University of Ibadan student email domain
    - Creates a User account
    '''
    def create_user(self, email, first_name, whatsapp_number, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not email.endswith("@stu.ui.edu.ng"):
            raise ValidationError("Only university student emails (@stu.ui.edu.ng) are allowed")

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, whatsapp_number=whatsapp_number)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    '''
    - Creates an admin account
    '''
    def create_superuser(self, email, first_name, password=None):
        if not email:
            raise ValueError("Superusers must have an email address")

        email = self.normalize_email(email)

        user = user = self.model(email=email, first_name=first_name, whatsapp_number="00000000000")
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    whatsapp_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?\d{9,15}$', message="Enter a valid WhatsApp number")]
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.email
