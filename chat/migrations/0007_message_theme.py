# Generated by Django 4.1.7 on 2023-04-29 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_rename_name_theme_newchat'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='Theme',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='message', to='chat.theme'),
        ),
    ]