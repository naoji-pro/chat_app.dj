# Generated by Django 4.1.7 on 2023-05-02 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0013_message_res_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='content',
        ),
        migrations.RemoveField(
            model_name='message',
            name='role',
        ),
    ]
