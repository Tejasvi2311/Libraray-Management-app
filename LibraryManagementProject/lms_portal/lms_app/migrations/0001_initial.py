# Generated by Django 5.0.3 on 2024-04-03 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.TextField()),
                ('author_name', models.CharField(max_length=200)),
                ('publication', models.TextField()),
                ('count', models.CharField(max_length=200)),
            ],
        ),
    ]
