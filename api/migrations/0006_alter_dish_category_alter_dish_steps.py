# Generated by Django 4.1 on 2023-04-30 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_category_type_remove_dish_cook_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.ManyToManyField(default='default_category', to='api.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='steps',
            field=models.CharField(blank=True, max_length=5000, verbose_name='Рецепт'),
        ),
    ]
