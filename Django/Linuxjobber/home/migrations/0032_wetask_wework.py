# Generated by Django 2.0.7 on 2019-01-27 17:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_auto_20190127_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='wetask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.TextField()),
                ('description', models.TextField()),
                ('task', models.CharField(max_length=50, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0)),
                ('types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.wetype')),
            ],
        ),
        migrations.CreateModel(
            name='wework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Done')], default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('send_task', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0)),
                ('due', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.wetask')),
                ('we_people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.wepeoples')),
            ],
        ),
    ]
