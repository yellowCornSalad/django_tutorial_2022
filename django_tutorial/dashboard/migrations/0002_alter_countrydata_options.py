# Generated by Django 4.0.3 on 2022-03-17 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='countrydata',
            options={'verbose_name_plural': '각 나라별 인구 데이터'},
        ),
    ]