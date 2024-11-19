from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_instructor = models.BooleanField(default=False)
    is_client = models.BooleanField(default=True)  # Asegúrate de tener este campo.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    specialty = models.CharField(max_length=100, blank=True, null=True)  # Solo para instructores

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Routine(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='routines')
    title = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(
        max_length=50,
        choices=[
            ('Beginner', 'Beginner'),
            ('Intermediate', 'Intermediate'),
            ('Advanced', 'Advanced'),
        ],
        default='Beginner'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Reservation(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='reservations')
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.username} -> {self.routine.title}"
