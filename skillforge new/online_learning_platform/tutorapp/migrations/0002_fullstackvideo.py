# Generated by Django 4.2.5 on 2024-05-13 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FullstackVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video_file', models.FileField(upload_to='videos/')),
            ],
        ),
    ]