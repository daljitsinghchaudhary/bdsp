# Generated by Django 2.2.3 on 2019-10-18 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20191015_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='Year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
