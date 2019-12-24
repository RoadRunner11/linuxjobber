# Generated by Django 2.0.7 on 2019-12-13 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20191213_1313'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0098_merge_20191212_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('extra_members', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('members_by_role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Role')),
            ],
        ),
    ]