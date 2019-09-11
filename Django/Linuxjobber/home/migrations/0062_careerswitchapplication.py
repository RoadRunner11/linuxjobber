# Generated by Django 2.0.7 on 2019-09-01 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0061_merge_20190806_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerSwitchApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('old_career', models.CharField(max_length=255)),
                ('resume', models.FileField(null=True, upload_to='resume')),
                ('cv_link', models.CharField(max_length=200, null=True)),
                ('new_career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.FullTimePostion')),
            ],
        ),
    ]
