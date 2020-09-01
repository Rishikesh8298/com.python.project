# Generated by Django 3.0.6 on 2020-07-13 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('correctAnswer', models.CharField(max_length=20)),
                ('totalQuestion', models.CharField(max_length=20)),
            ],
        ),
    ]
