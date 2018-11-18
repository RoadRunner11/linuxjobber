# Generated by Django 2.0.8 on 2018-11-10 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoStudentRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField(default=6)),
                ('user', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='classroom.DjangoStudent')),
            ],
        ),
    ]
