# Generated by Django 2.2.1 on 2019-07-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20190618_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='profile_image'),
        ),
    ]