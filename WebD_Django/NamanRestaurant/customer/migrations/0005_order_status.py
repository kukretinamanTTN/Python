# Generated by Django 5.1.7 on 2025-03-20 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_fooditem_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=10),
        ),
    ]
