from django.db import models

# Create your models here.
class Lecture(models.Model):
    lecture = models.CharField(max_length=100)
    lecture_content1 = models.TextField(max_length=500, null=True, blank=True)
    lecture_content2 = models.TextField(max_length=500, null=True, blank=True)
    lecture_content3 = models.TextField(max_length=500, null=True, blank=True)
    lecture_content4 = models.TextField(max_length=500, null=True, blank=True)
    lecture_content5 = models.TextField(max_length=500, null=True, blank=True)
    lecture_content6 = models.TextField(max_length=500, null=True, blank=True)