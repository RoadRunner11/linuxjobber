# Generated by Django 2.0.7 on 2020-01-26 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0111_auto_20200105_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperienceeligibility',
            name='pdf',
            field=models.FileField(null=True, upload_to='resume'),
        ),
        migrations.AddField(
            model_name='workexperienceisa',
            name='pdf',
            field=models.FileField(null=True, upload_to='resume'),
        ),
    ]
