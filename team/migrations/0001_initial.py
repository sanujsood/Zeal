# Generated by Django 3.1.1 on 2020-09-26 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('designation', models.CharField(max_length=45)),
                ('images', models.ImageField(default='', upload_to='images/team')),
                ('linkedin', models.URLField()),
                ('status', models.CharField(choices=[('member', 'member'), ('developer', 'developer'), ('cord', 'cord'), ('fac', 'fac')], max_length=128)),
            ],
        ),
    ]