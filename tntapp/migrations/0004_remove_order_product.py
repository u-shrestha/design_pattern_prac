# Generated by Django 3.1.2 on 2021-01-29 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tntapp', '0003_auto_20210129_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
    ]