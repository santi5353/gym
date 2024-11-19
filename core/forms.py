from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User, Reservation



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_instructor', 'is_client']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'specialty']

from .models import Routine

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['title', 'description', 'difficulty']
        
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = []