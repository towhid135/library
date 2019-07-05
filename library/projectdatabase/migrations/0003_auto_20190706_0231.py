# Generated by Django 2.2 on 2019-07-05 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectdatabase', '0002_auto_20190705_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signuptable',
            name='id',
        ),
        migrations.AddField(
            model_name='signuptable',
            name='ID',
            field=models.CharField(default='null', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='signuptable',
            name='department',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AddField(
            model_name='signuptable',
            name='name',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='signuptable',
            name='answer',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='signuptable',
            name='password',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='signuptable',
            name='role',
            field=models.CharField(default='null', max_length=15),
        ),
        migrations.AlterField(
            model_name='signuptable',
            name='sequrity',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='signuptable',
            name='user',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
