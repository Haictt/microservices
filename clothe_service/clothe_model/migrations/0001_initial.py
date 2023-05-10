# Generated by Django 4.1.7 on 2023-03-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clothe_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothe_id', models.CharField(max_length=10)),
                ('product_category', models.CharField(max_length=50)),
                ('clothe_name', models.CharField(max_length=100)),
                ('availability', models.CharField(max_length=15)),
                ('price', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
            ],
        ),
    ]