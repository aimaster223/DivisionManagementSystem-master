# Generated by Django 3.1.4 on 2021-01-06 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0011_auto_20210105_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email_attendance_doc_day3',
            field=models.BooleanField(default=True, help_text='Receive an email when it has been 3 days since aattendance point was given but a signed documenthas not been uploaded', verbose_name='3 Days Past Due Attendance'),
        ),
    ]
