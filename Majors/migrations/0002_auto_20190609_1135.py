# Generated by Django 2.1.7 on 2019-06-09 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Majors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='summarie',
            name='subject_major',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Majors.Major'),
        ),
        migrations.AlterField(
            model_name='summarie',
            name='subject_name',
            field=models.CharField(max_length=200),
        ),
    ]
