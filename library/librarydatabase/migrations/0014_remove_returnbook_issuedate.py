# Generated by Django 2.2 on 2019-07-25 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarydatabase', '0013_auto_20190721_0101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='returnbook',
            name='issuedate',
        ),
    ]
