# Generated by Django 2.2 on 2019-07-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarydatabase', '0010_auto_20190708_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='testing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myname', models.CharField(default='null', max_length=200)),
                ('password', models.CharField(default='null', max_length=200)),
            ],
        ),
    ]