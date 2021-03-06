# Generated by Django 4.0.3 on 2022-03-30 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hall', '0014_hallpresence_in_transit'),
    ]

    operations = [
        migrations.AddField(
            model_name='hallpresence',
            name='first_name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='hallpresence',
            name='last_name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='hallpresence',
            name='mobile_no',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='hallpresence',
            name='roll_no',
            field=models.IntegerField(null=True),
        ),
    ]
