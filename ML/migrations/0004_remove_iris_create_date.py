# Generated by Django 4.2 on 2024-04-13 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ML', '0003_alter_iris_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iris',
            name='create_date',
        ),
    ]
