# Generated by Django 4.0.1 on 2023-04-28 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_roommember_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roommember',
            name='uid',
        ),
    ]