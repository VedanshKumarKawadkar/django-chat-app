# Generated by Django 4.0.6 on 2024-03-10 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_alter_room_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='slug',
        ),
    ]
