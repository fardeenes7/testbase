# Generated by Django 4.1.1 on 2023-09-13 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0015_alter_exam_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='exam_files'),
        ),
    ]