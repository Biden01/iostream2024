from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    STATUS = (
        ('Student', 'Студент'),
        ('School', 'Мектеп оқушысы'),
        ('Teacher', 'Мұғалім'),
        ('Other', 'Басқа')
    )

    city = models.CharField(max_length=50, null=True, blank=True, default='')
    status = models.CharField(max_length=10, choices=STATUS, default='Student')
    birth_date = models.DateField(null=True, blank=True, default='2001-09-11')
    phone = models.CharField(max_length=11, null=True, blank=True, default='')
