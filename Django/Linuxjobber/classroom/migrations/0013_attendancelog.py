# Generated by Django 2.0.7 on 2019-03-09 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0043_tryfreerecord'),
        ('classroom', '0012_auto_20190227_0212'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Groupclass')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='group_attendance', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
