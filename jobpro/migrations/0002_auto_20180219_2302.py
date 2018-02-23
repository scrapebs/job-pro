# Generated by Django 2.0 on 2018-02-19 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobpro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('salary', models.IntegerField(default=60000)),
                ('actual', models.BooleanField(default=True)),
                ('profession', models.CharField(choices=[('AV', 'Автомобильный бизнес'), ('BA', 'Банки, инвестиции'), ('SE', 'Безопасность'), ('SP', 'Спорт'), ('IT', 'Информационные технологии, интернет, телеком'), ('SC', 'Наука, образование'), ('TR', 'Продажи'), ('LA', 'Юристы')], default='AV', max_length=2)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='favourite',
            name='vacancy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobpro.Vacancy'),
        ),
    ]