# Generated by Django 2.2.5 on 2019-11-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=70)),
                ('lastname', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('DOB', models.DateTimeField()),
            ],
        ),
    ]
