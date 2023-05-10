# Generated by Django 4.1.7 on 2023-03-28 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shoe_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoe_id', models.CharField(max_length=10)),
                ('product_category', models.CharField(max_length=50)),
                ('shoe_name', models.CharField(max_length=100)),
                ('availability', models.CharField(max_length=15)),
                ('price', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('size', models.CharField(max_length=10)),
            ],
        ),
    ]
