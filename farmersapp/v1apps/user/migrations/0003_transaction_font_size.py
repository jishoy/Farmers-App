# Generated by Django 2.2 on 2021-02-12 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_expiringtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='font_size',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
