# Generated by Django 4.2.1 on 2023-05-16 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-05-12'),
            preserve_default=False,
        ),
    ]
