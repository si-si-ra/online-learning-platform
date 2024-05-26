# Generated by Django 4.2.5 on 2024-05-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorapp', '0005_assignment_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='status',
            field=models.CharField(choices=[('Submitted', 'Submitted'), ('Graded', 'Graded'), ('Late Submission', 'Late Submission'), ('Not Submitted', 'Not Submitted')], default='Not Submitted', max_length=50),
        ),
    ]