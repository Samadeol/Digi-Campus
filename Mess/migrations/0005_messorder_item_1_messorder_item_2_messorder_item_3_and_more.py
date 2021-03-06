# Generated by Django 4.0.3 on 2022-03-18 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Mess', '0004_messorder_ordereddate'),
    ]

    operations = [
        migrations.AddField(
            model_name='messorder',
            name='item_1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='item_2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='item_3',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='item_4',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='item_5',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='item_6',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='price_1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='price_2',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='price_3',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='price_4',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='price_5',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='price_6',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='quantity_1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='quantity_2',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='quantity_3',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='quantity_4',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='quantity_5',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='quantity_6',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='messorder',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
