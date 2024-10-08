# Generated by Django 4.2.8 on 2024-08-12 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_category_de_product_category_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_de',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_es',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_fr',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_es',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_fr',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_es',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_fr',
        ),
        migrations.AddField(
            model_name='category',
            name='name_de',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_de',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_de',
            field=models.CharField(max_length=200, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=200, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='name'),
        ),
    ]
