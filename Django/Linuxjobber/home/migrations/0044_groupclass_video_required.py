# Generated by Django 2.0.7 on 2019-03-11 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_tryfreerecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupclass',
            name='video_required',
            field=models.BooleanField(default=False),
        ),
    ]
