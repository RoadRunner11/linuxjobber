# Generated by Django 2.0.7 on 2019-03-10 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0013_attendancelog'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancelog',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
