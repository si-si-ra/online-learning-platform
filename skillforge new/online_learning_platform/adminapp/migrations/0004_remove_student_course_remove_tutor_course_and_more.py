# Generated by Django 4.2.5 on 2024-05-06 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_tutor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='course',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Tutor',
        ),
    ]