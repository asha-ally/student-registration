# Generated by Django 2.2.1 on 2019-10-17 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_remove_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teachers',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='teacher.Teacher'),
        ),
    ]
