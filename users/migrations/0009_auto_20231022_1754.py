# Generated by Django 3.2.4 on 2023-10-22 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['is_read', '-created']},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='isRead',
            new_name='is_read',
        ),
    ]