# Generated by Django 2.0.7 on 2019-04-25 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_is_subscribed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_subscribed',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=1),
        ),
    ]