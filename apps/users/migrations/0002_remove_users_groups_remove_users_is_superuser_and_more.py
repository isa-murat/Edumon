# Generated by Django 5.0.1 on 2024-01-14 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='users',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_permissions',
        ),
    ]
