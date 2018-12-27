# Generated by Django 2.0.1 on 2018-11-28 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Courses', '0005_auto_20181128_0126'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=1)),
                ('User', models.ForeignKey(limit_choices_to={'role': 4}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.Course')),
            ],
        ),
    ]