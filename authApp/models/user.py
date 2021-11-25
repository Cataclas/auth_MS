from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, usu_correo, password=None):
        if not usu_correo:
            raise ValueError('Users must have an username')
        user=self.model(username=usu_correo)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,  usu_correo, password):
        user = self.create_user(
            username=usu_correo,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField('usu_id',primary_key=True)
    usu_nombres = models.CharField('Nombres',max_length=50)
    usu_apellidos = models.CharField('Apellidos',max_length=50)
    usu_correo = models.EmailField('Correo',max_length=150,unique=True)
    usu_cargo = models.CharField('Cargo',max_length=30)
    password = models.CharField('Contraseña',max_length=256)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'usu_correo'