# Generated by Django 5.1.1 on 2024-10-21 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_delete_orderview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-order_date']},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='created',
            new_name='order_date',
        ),
    ]
