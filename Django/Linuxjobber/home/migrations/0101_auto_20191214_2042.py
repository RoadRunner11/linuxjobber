# Generated by Django 2.0.7 on 2019-12-14 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0100_auto_20191214_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailgroup',
            name='exclude_clause',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emailgroup',
            name='where_clause',
            field=models.TextField(blank=True, null=True),
        ),
    ]
