# Generated by Django 4.1.7 on 2023-05-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_message_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='role',
            field=models.CharField(default='system', max_length=10),
        ),
    ]
