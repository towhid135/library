# Generated by Django 2.2 on 2019-07-16 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarydatabase', '0011_testing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signtable',
            old_name='answer',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='signtable',
            name='sequrity',
        ),
    ]
