# Generated by Django 5.1.1 on 2024-10-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='application_form',
        ),
        migrations.AddField(
            model_name='applicant',
            name='Combination',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='field_of_study',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='next_class',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Application_Form',
        ),
    ]
