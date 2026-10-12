from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser

# Create your models here.

class RoleChoices(models.TextChoices):

    ADMIN='admin','admin'
    STUDENT='student','student'

class Profile(AbstractUser):

    role=models.CharField(max_length=10,choices=RoleChoices.choices)

    def __str__(self):

        return self.username

    class Meta:


        verbose_name='Profiles'

        verbose_name_plural='Profiles'
