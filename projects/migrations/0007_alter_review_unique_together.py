# Generated by Django 3.2.4 on 2023-10-20 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_profile_image'),
        ('projects', '0006_auto_20231020_2206'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'project')},
        ),
    ]
