# Generated by Django 4.1.3 on 2023-02-18 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_listproductindustry_oder_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='listproductindustry',
            name='Information_English',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listproductindustry',
            name='Title_English',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]