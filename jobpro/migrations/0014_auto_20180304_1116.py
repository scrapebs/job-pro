# Generated by Django 2.0 on 2018-03-04 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobpro', '0013_auto_20180303_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='email',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='cv',
            name='phone',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]