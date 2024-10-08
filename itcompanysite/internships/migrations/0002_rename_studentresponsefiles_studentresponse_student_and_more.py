# Generated by Django 4.2.6 on 2024-09-22 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('accounts', '0006_alter_file_document_name_alter_file_document_text'),
        ('internships', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentresponse',
            old_name='studentResponseFiles',
            new_name='student',
        ),
        migrations.AlterField(
            model_name='internship',
            name='all_places',
            field=models.IntegerField(verbose_name='Всего мест'),
        ),
        migrations.AlterField(
            model_name='internship',
            name='available_places',
            field=models.IntegerField(verbose_name='Доступных мест'),
        ),
        migrations.AlterField(
            model_name='internship',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='companies.company', verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='internship',
            name='company_address',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='companies.companyaddress', verbose_name='Адрес компании'),
        ),
        migrations.AlterField(
            model_name='internship',
            name='date_end',
            field=models.DateField(verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='internship',
            name='date_start',
            field=models.DateField(verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='internship',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='internship',
            name='salary',
            field=models.IntegerField(verbose_name='Зарплата'),
        ),
        migrations.AlterField(
            model_name='internship',
            name='time_type_work',
            field=models.TextField(verbose_name='Тип рабочего времени'),
        ),
        migrations.AlterField(
            model_name='studentresponse',
            name='data_response',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата отклика'),
        ),
        migrations.AlterField(
            model_name='studentresponse',
            name='response_text',
            field=models.TextField(blank=True, verbose_name='Текст отклика'),
        ),
        migrations.CreateModel(
            name='StudentResponseFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.file')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internships.studentresponse')),
            ],
        ),
    ]
