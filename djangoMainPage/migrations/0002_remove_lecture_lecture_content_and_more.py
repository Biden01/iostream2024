# Generated by Django 4.2.13 on 2024-06-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoMainPage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='lecture_content',
        ),
        migrations.AddField(
            model_name='lecture',
            name='lecture_content1',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='lecture_content2',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='lecture_content3',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='lecture_content4',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='lecture_content5',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='lecture_content6',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecture',
            field=models.CharField(max_length=100),
        ),
    ]
