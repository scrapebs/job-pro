# Generated by Django 2.0 on 2018-03-02 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobpro', '0010_auto_20180228_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orginfo',
            name='organisation',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='info', to=settings.AUTH_USER_MODEL),
        ),
    ]
