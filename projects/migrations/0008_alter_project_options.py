# Generated by Django 3.2.4 on 2023-10-22 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_review_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]
