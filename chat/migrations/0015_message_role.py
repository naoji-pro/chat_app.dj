# Generated by Django 4.1.7 on 2023-05-07 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0014_remove_message_content_remove_message_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='role',
            field=models.CharField(default='system', max_length=255),
        ),
    ]
