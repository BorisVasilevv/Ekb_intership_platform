# Generated by Django 4.2.6 on 2024-09-22 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_file_document_name_alter_file_document_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='document_name',
            field=models.TextField(default='fileea6f3f8a-d098-4214-be76-48ae48a951da', verbose_name='document_name'),
        ),
        migrations.AlterField(
            model_name='file',
            name='document_text',
            field=models.FileField(upload_to='files/ad21f64e-000c-4903-97dd-af18516842a6', verbose_name='document_text'),
        ),
    ]
