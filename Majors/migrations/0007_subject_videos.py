# Generated by Django 2.1.7 on 2019-06-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Majors', '0006_auto_20190628_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='videos',
            field=models.URLField(blank=True),
        ),
    ]
