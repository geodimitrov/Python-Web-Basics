# Generated by Django 3.2.4 on 2021-06-11 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20210611_1013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'people'},
        ),
    ]
