# Generated by Django 3.0.6 on 2020-07-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='name',
        ),
        migrations.AddField(
            model_name='main',
            name='adminName',
            field=models.CharField(default='admin', max_length=15),
        ),
        migrations.AddField(
            model_name='main',
            name='password',
            field=models.CharField(default='application', max_length=15),
        ),
    ]
