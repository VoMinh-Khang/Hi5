# Generated by Django 4.1.4 on 2023-01-01 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accouts', '0002_alter_account_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='userid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
