# Generated by Django 2.0.7 on 2019-02-10 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_wetask_weight'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='wetask',
            unique_together={('types', 'weight')},
        ),
    ]
