# Generated by Django 4.2.6 on 2024-09-22 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_merge_20240922_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='document_name',
            field=models.TextField(default='file2adf6ebc-031a-478d-8dfe-2ee4f916a63c', verbose_name='document_name'),
        ),
        migrations.AlterField(
            model_name='file',
            name='document_text',
            field=models.FileField(upload_to='files/9cae1cbf-3d13-4bd2-bdbe-d6167819749a', verbose_name='document_text'),
        ),
    ]
