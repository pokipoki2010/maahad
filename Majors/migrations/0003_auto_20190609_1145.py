# Generated by Django 2.1.7 on 2019-06-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Majors', '0002_auto_20190609_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='major_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='summarie',
            name='subject_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
