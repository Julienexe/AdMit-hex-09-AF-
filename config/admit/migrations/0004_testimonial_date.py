# Generated by Django 5.1.1 on 2024-10-09 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admit', '0003_remove_applicant_testimonial_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]