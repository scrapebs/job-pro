# Generated by Django 2.0 on 2018-02-28 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobpro', '0008_auto_20180225_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='org_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orginfo', to='jobpro.OrgInfo'),
        ),
    ]
