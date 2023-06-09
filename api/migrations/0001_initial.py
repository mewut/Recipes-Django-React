# Generated by Django 4.1 on 2023-04-26 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Завтрак', 'Завтрак'), ('Обед', 'Обед'), ('Ужин', 'Ужин'), ('Перекус', 'Перекус')], max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, unique=True)),
                ('ingredients', models.CharField(max_length=255)),
                ('steps', models.CharField(max_length=2255, null=True)),
                ('cook_time', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
