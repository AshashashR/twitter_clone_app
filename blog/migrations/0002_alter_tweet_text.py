# Generated by Django 3.2 on 2021-05-10 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.CharField(default='', max_length=280, verbose_name='Text'),
        ),
    ]
