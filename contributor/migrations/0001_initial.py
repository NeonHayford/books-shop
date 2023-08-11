# Generated by Django 4.2.4 on 2023-08-11 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='book id')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, verbose_name='slug')),
                ('category', models.CharField(max_length=70)),
                ('description', models.TextField(blank=True)),
                ('author', models.CharField(max_length=150)),
                ('published', models.DateField(blank=True, null=True)),
                ('added_date', models.DateField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, default=3.99, max_digits=15)),
            ],
        ),
    ]
