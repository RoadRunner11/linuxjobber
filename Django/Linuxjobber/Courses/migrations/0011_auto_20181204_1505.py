# Generated by Django 2.0.1 on 2018-12-04 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0010_topicstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicstatus',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.CourseTopic'),
        ),
        migrations.AlterField(
            model_name='topicstatus',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
