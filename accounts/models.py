from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
class Acconunt(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)



    #required

    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_nanme', 'last_name']

    def __str__(self):
        return self.email
    

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True

# Create your models here.
