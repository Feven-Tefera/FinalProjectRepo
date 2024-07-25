from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    subcity=models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.firstname + self.lastname
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='account_users',
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='account_user_permissions',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
    )