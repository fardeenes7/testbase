# Generated by Django 4.1.1 on 2022-09-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_alter_class_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='exam_date',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='class',
            name='code',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
    ]
