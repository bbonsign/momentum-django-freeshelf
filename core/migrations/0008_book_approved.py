# Generated by Django 3.0.3 on 2020-03-02 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200229_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
