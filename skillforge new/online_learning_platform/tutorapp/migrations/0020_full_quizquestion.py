# Generated by Django 4.2.5 on 2024-05-18 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorapp', '0019_full_assignment_full_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Full_QuizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=255)),
                ('correct_answer', models.CharField(max_length=255)),
                ('option_a', models.CharField(max_length=255)),
                ('option_b', models.CharField(max_length=255)),
                ('option_c', models.CharField(max_length=255)),
                ('option_d', models.CharField(max_length=255)),
            ],
        ),
    ]
