from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
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
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        default='',
        validators=[RegexValidator('\+[0-9]{1}\([0-9]{3}\)[0-9]{3}\-[0-9]{4}')]
    )
    subscribe = models.BooleanField(default=False)