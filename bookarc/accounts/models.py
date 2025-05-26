from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('reader', 'Reader'),
        ('librarian', 'Librarian'),
    ]
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    librarian_code = models.CharField(
        max_length=4, blank=True,
        help_text="Required if role is Librarian"
    )

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.role == 'librarian' and not self.librarian_code:
            raise ValidationError("Librarian code is required.")
