# Generated by Django 2.0 on 2018-03-03 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobpro', '0011_auto_20180302_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='org_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orginfo', to='jobpro.OrgInfo'),
        ),
    ]
