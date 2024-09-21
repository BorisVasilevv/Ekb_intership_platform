# Generated by Django 4.2.6 on 2024-09-21 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0005_delete_companytag_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_places', models.IntegerField(verbose_name='all_places')),
                ('available_places', models.IntegerField(verbose_name='available_places')),
                ('time_type_work', models.TextField(verbose_name='time_type_work')),
                ('date_start', models.DateField(verbose_name='date_start')),
                ('date_end', models.DateField(verbose_name='date_end')),
                ('salary', models.IntegerField(verbose_name='salary')),
                ('description', models.TextField(default='', verbose_name='description')),
                ('company', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='companies.company')),
                ('company_address', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='companies.companyaddress')),
            ],
        ),
    ]
