# Generated by Django 2.2 on 2019-07-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarydatabase', '0012_auto_20190716_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signtable',
            name='department',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='signtable',
            name='memberid',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='signtable',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='signtable',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='signtable',
            name='phone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='signtable',
            name='role',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='signtable',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
