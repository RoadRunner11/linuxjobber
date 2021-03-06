# Generated by Django 2.0.7 on 2019-12-11 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessageWithProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=400)),
                ('the_type', models.CharField(default='plain', max_length=10)),
                ('timestamp', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'classroom_chatmessage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('profile_img', models.TextField(default='https://res.cloudinary.com/louiseyoma/        image/upload/v1546701687/profile_pic.png')),
            ],
            options={
                'db_table': 'users_customuser',
                'managed': False,
            },
        ),
    ]
