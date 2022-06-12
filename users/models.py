from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, username, email, name, last_name, password, is_staff, is_superuser, **extra_fileds):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fileds
        )
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_user(self, username, email, name, last_name, password = None, **extra_fileds):
        return self._create_user(username, email, name, last_name, password, False, False, **extra_fileds)

    def create_superuser(self, username, email, name, last_name, password = None, **extra_fileds):
        return self._create_user(username, email, name, last_name, password, True, True, **extra_fileds)

#* Tabla de Usuarios
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField(max_length = 255, unique = True, verbose_name = 'Correo electronico')

    name = models.CharField(max_length = 255, blank = True, verbose_name = 'Nombres', null = True)
    last_name = models.CharField(max_length = 255, blank = True, verbose_name = 'Apellidos', null = True)

    image = models.TextField(null = True, blank = True, verbose_name = 'Imagen de perfil', default = 'https://res.cloudinary.com/ebanisteria/image/upload/v1655070601/64572_q5quxt.png')

    rolUser = models.CharField(max_length = 30, blank = False, null = False, default = 'Cliente', verbose_name = 'Rol de usuarios')

    direccion = models.TextField(null = True, blank = True)
    edad = models.IntegerField(null = True, blank = True)

    is_active = models.BooleanField(default = True, verbose_name = 'activo')
    is_staff = models.BooleanField(default = False, verbose_name = 'staff')

    historical = HistoricalRecords()

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name', 'rolUser']

    def __str__(self):
        return f'{self.name} {self.last_name}'

