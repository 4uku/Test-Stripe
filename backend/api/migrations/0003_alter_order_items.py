# Generated by Django 4.1.1 on 2022-09-13 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(null=True, to='api.item', verbose_name='Товары'),
        ),
    ]