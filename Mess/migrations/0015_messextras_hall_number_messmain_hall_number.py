# Generated by Django 4.0.3 on 2022-03-25 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mess', '0014_rename_messmenu_messextras_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='messextras',
            name='hall_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='messmain',
            name='hall_number',
            field=models.IntegerField(null=True),
        ),
    ]
