# Generated by Django 2.1.1 on 2019-04-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0003_auto_20190414_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='sid',
            field=models.IntegerField(),
        ),
    ]