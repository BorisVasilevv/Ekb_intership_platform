from django.contrib import admin
from .models import Company, Category, Subcategory, CompanyCategory, Favorite, \
    Address, City, CompanyAddress, Tag, CompanyTag
# Register your models here.


# class MyAdminModel(admin.ModelAdmin):
#     exclude = ('style_name',)


admin.site.register(Company)
admin.site.register(Favorite)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(CompanyCategory)
admin.site.register(Address)
admin.site.register(City)
admin.site.register(CompanyAddress)
admin.site.register(Tag)
admin.site.register(CompanyTag)
