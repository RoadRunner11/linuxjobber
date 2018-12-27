# Generated by Django 2.0.1 on 2018-12-05 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0013_remove_topicstatus_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='aws_credential_required',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='lab_submission_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'none'), (1, 'submit by uploading document'), (2, 'submit by machine ID'), (3, 'submit from repo')], default=1),
        ),
    ]