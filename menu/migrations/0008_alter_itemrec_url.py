# Generated by Django 5.0.2 on 2024-02-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_itemrec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemrec',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]