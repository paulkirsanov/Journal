# Generated by Django 4.2.1 on 2023-06-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogform',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
