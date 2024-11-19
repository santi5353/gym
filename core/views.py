from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, CustomUserCreationForm, RoutineForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Routine, Reservation



def home(request):
    return render(request, 'core/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'core/edit_profile.html', {'form': form})

@login_required
def my_routines(request):
    if not request.user.is_instructor:
        return redirect('home')
    routines = Routine.objects.filter(instructor=request.user).prefetch_related('reservations__client')
    return render(request, 'core/my_routines.html', {'routines': routines})

@login_required
def create_routine(request):
    if not request.user.is_instructor:
        return redirect('home')
    if request.method == 'POST':
        form = RoutineForm(request.POST)
        if form.is_valid():
            routine = form.save(commit=False)
            routine.instructor = request.user
            routine.save()
            return redirect('my_routines')
    else:
        form = RoutineForm()
    return render(request, 'core/create_routine.html', {'form': form})

def all_routines(request):
    routines = Routine.objects.all()
    return render(request, 'core/all_routines.html', {'routines': routines})

@login_required
def reserve_class(request, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)
    if not request.user.is_client:
        return redirect('home')

    if request.method == 'POST':
        reservation = Reservation(client=request.user, routine=routine)
        reservation.save()
        return redirect('all_routines')

    return render(request, 'core/reserve_class.html', {'routine': routine})