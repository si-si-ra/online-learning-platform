# Generated by Django 4.2.5 on 2024-05-25 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorapp', '0020_full_quizquestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='full_note',
            name='title',
            field=models.CharField(default='Untitled Note', max_length=200),
        ),
    ]