# Generated by Django 4.1.2 on 2022-10-26 15:13

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0006_alter_vacancy_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('data', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.CharField(max_length=250, verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(verbose_name='Описание вакансии'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Заголовок ваканскии'),
        ),
    ]
