# Generated by Django 3.0.6 on 2020-07-27 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0003_auto_20200727_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='count',
        ),
    ]