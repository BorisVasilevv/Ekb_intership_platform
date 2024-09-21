from . import views
from django.urls import path, include

urlpatterns = [

    path('', views.companies, name='companies'),
    path('search/', views.search, name='search'),
    path('<str:category_or_subcategory_name>/', views.companies_per_category_subcategory, name='companies_per_subcategory'),
    path('add_to_favorites/<int:company_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('<str:category_or_subcategory_name>/add_to_favorites/<int:company_id>/', views.add_to_favorites_with_category, name='add_to_favorites_with_category')
]
