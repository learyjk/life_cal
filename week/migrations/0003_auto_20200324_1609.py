# Generated by Django 3.0.4 on 2020-03-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('week', '0002_auto_20200324_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]