# Generated by Django 4.1.7 on 2023-05-08 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0016_remove_message_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='role',
            field=models.CharField(default='system', max_length=255),
        ),
    ]
