# Generated by Django 2.1.7 on 2019-02-27 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190227_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='credit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
