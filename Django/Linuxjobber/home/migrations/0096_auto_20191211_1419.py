# Generated by Django 2.2.2 on 2019-12-11 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0095_auto_20191211_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workexperienceisa',
            old_name='Current_Annual_Income',
            new_name='current_annual_Income',
        ),
        migrations.RenameField(
            model_name='workexperienceisa',
            old_name='Employment_status',
            new_name='employment_status',
        ),
        migrations.RenameField(
            model_name='workexperienceisa',
            old_name='Estimated_date_of_program_completion',
            new_name='estimated_date_of_program_completion',
        ),
        migrations.RenameField(
            model_name='workexperienceisa',
            old_name='Highest_level_education',
            new_name='highest_level_education',
        ),
        migrations.RenameField(
            model_name='workexperienceisa',
            old_name='is_Signed_isa',
            new_name='is_signed_isa',
        ),
        migrations.RenameField(
            model_name='workexperienceisa',
            old_name='Monthly_House_Payment',
            new_name='monthly_house_Payment',
        ),
    ]
