from django.urls import path
from .views import register, login_view, logout_view, home,edit_profile,  my_routines, create_routine, all_routines, reserve_class  # Asegúrate de incluir `home`

urlpatterns = [
    path('', home, name='home'),  # Página de inicio
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('routines/', my_routines, name='my_routines'),
    path('routines/create/', create_routine, name='create_routine'),
    path('routines/all/', all_routines, name='all_routines'),
    path('routines/<int:routine_id>/reserve/', reserve_class, name='reserve_class'),



]
