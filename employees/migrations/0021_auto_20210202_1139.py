# Generated by Django 3.1.4 on 2021-02-02 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0020_auto_20210128_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counseling',
            name='assigned_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hold',
            name='assigned_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='safetypoint',
            name='assigned_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='settlement',
            name='assigned_by',
            field=models.IntegerField(),
        ),
    ]