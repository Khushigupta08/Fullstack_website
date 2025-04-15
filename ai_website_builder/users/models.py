from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure email is unique
    USERNAME_FIELD = 'email'  # This ensures authentication is based on email
    REQUIRED_FIELDS = ['username']
    # Override groups field with a unique related_name
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Unique related_name
        blank=True,
    )

    # Override user_permissions field with a unique related_name
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Unique related_name
        blank=True,
    )
