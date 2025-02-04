# Generated by Django 5.1.2 on 2024-10-24 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_merge_20241022_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='deactivated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_deactivated',
            field=models.BooleanField(default=False),
        ),
    ]
