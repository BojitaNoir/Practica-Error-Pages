# Generated by Django 5.1.5 on 2025-02-05 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='token',
        ),
    ]
