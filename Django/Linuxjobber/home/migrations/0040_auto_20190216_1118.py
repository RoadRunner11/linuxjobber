# Generated by Django 2.0.7 on 2019-02-16 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_auto_20190210_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wetask',
            options={'ordering': ('types', 'weight')},
        ),
        migrations.AlterModelOptions(
            name='wework',
            options={'ordering': ('we_people', 'weight')},
        ),
    ]
