# Generated by Django 3.1.1 on 2020-09-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20200918_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='document',
            field=models.FileField(upload_to=''),
        ),
    ]
