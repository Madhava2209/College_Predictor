# Generated by Django 3.0.3 on 2020-03-06 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('College_Predictor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='college',
            old_name='Branch',
            new_name='branch',
        ),
        migrations.RenameField(
            model_name='college',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='college',
            old_name='College_ID',
            new_name='college_ID',
        ),
        migrations.RenameField(
            model_name='college',
            old_name='College_Name',
            new_name='college_Name',
        ),
        migrations.RenameField(
            model_name='college',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='college',
            old_name='Rank',
            new_name='rank',
        ),
    ]