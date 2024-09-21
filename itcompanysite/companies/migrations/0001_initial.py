# Generated by Django 4.2.6 on 2024-09-21 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=150, verbose_name='street')),
                ('home_number', models.CharField(max_length=15, verbose_name='home_number')),
                ('coordinate_x', models.FloatField(blank=True, null=True)),
                ('coordinate_y', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(choices=[('Собственный IT-продукт', 'Собственный IT-продукт'), ('Заказная разработка', 'Заказная разработка'), ('Другое', 'Другое'), ('Неопределенный', 'Неопределенный')], max_length=100, verbose_name='category_name')),
                ('color', models.CharField(default='gray', max_length=25, verbose_name='color')),
                ('description', models.TextField(default='', verbose_name='description')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('coordinate_x', models.FloatField()),
                ('coordinate_y', models.FloatField()),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('logotype', models.ImageField(upload_to='companies/logo/img', verbose_name='logotype')),
                ('short_description', models.TextField(verbose_name='short_description')),
                ('url', models.CharField(max_length=200, verbose_name='url')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='phone')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='CompanyAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='companies.address')),
                ('company', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='companies.company')),
            ],
            options={
                'verbose_name': 'Адрес компании',
                'verbose_name_plural': 'Адреса компаний',
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization_name', models.TextField(verbose_name='specialization_name')),
            ],
            options={
                'verbose_name': 'Специализация',
                'verbose_name_plural': 'Специализации',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(choices=[('Стартапы с IT решениями', 'Стартапы с IT решениями'), ('Сопровождение популярных массовых ИТ продуктов', 'Сопровождение популярных массовых ИТ продуктов'), ('Веб-студии', 'Веб-студии'), ('Большие ИТ - компании', 'Большие ИТ - компании'), ('B2G', 'B2G'), ('Разработка игр', 'Разработка игр'), ('Компьютерная безопасность', 'Компьютерная безопасность'), ('Неопределенный', 'Неопределенный')], max_length=100, verbose_name='subcategory_name')),
                ('color', models.CharField(default='gray', max_length=25, verbose_name='color')),
                ('description', models.TextField(default='', verbose_name='description')),
                ('company_category', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='companies.category')),
            ],
            options={
                'verbose_name': 'CompanySubcategory',
                'verbose_name_plural': 'CompanySubcategories',
            },
        ),
        migrations.CreateModel(
            name='InternshipSpecialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_address', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='companies.companyaddress')),
                ('specialization', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='companies.specialization')),
            ],
            options={
                'verbose_name': 'Специализация у стажировки',
                'verbose_name_plural': 'Специализации стажировок',
            },
        ),
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('file', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.file')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='companies.city'),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'company')},
            },
        ),
        migrations.CreateModel(
            name='CompanyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.subcategory')),
            ],
            options={
                'verbose_name': 'CompanyCategory',
                'verbose_name_plural': 'CompanyCategories',
                'unique_together': {('subcategory', 'company')},
            },
        ),
    ]
