# Generated by Django 2.2.7 on 2019-11-06 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='user name'),
        ),
    ]