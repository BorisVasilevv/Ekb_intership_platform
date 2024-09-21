cd ..
..\venv\Scripts\Activate

python manage.py migrate

python manage.py loaddata .\companies\fixtures\categories_data_utf8.json
python manage.py loaddata .\companies\fixtures\subcategories_data_utf8.json
python manage.py loaddata .\companies\fixtures\companies_data_utf8.json
python manage.py loaddata .\companies\fixtures\company_categories_data_utf8.json
python manage.py loaddata .\companies\fixtures\cities_data_utf8.json
python manage.py loaddata .\companies\fixtures\address_data_utf8.json
python manage.py loaddata .\companies\fixtures\company_address_data_utf8.json
python manage.py loaddata .\companies\fixtures\tag_data_utf8.json
python manage.py loaddata .\companies\fixtures\company_tag_data_utf8.json
python manage.py loaddata .\companies\fixtures\user_data_utf8.json
python manage.py loaddata .\companies\fixtures\permission_data_utf8.json
python manage.py loaddata .\companies\fixtures\favorite_data_utf8.json