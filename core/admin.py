from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile, Routine

class UserAdmin(BaseUserAdmin):
    # Configurar los campos que se mostrarán en la lista de usuarios
    list_display = ('username', 'email', 'is_instructor', 'is_client', 'is_staff')
    list_filter = ('is_instructor', 'is_client', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ()
    
    # Configurar los campos que se mostrarán al editar un usuario
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email',)}),
        ('Roles', {'fields': ('is_instructor', 'is_client', 'is_staff', 'is_superuser')}),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_instructor', 'is_client')}
        ),
    )

# Registrar el modelo personalizado
admin.site.register(User, UserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'specialty')
    search_fields = ('user__username', 'bio')

@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'difficulty', 'created_at')
    search_fields = ('title', 'instructor__username')
    list_filter = ('difficulty',)
