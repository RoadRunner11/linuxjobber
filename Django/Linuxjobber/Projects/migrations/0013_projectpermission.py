# Generated by Django 2.0.7 on 2019-02-01 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Projects', '0012_auto_20190201_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.ProjectCourse')),
                ('user', models.ForeignKey(limit_choices_to={'role': 4}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
