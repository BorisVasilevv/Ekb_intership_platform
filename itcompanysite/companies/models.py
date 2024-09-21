from django.db import models
from .namehelper import CompanyName
from django.contrib.auth import get_user_model
from .utils import geocoder


User = get_user_model()

class Category(models.Model):
    CATEGORY_NAME = (
        (CompanyName.CONST_SELF_PRODUCT, CompanyName.CONST_SELF_PRODUCT),
        (CompanyName.CONST_CUSTOM_DEV, CompanyName.CONST_CUSTOM_DEV),
        (CompanyName.CONST_OTHER, CompanyName.CONST_OTHER),
        (CompanyName.CONST_NONE_TYPE, CompanyName.CONST_NONE_TYPE)
    )

    category_name = models.CharField('category_name', max_length=100, choices=CATEGORY_NAME)
    color = models.CharField('color', max_length=25, default="gray")
    description = models.TextField('description', default="")

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        match self.category_name:
            case CompanyName.CONST_SELF_PRODUCT:
                self.style_name = 'self_product'
            case CompanyName.CONST_CUSTOM_DEV:
                self.style_name = 'custom_dev'
            case CompanyName.CONST_OTHER:
                self.style_name = 'other'
            case CompanyName.CONST_NONE_TYPE:
                self.style_name = 'none_type'
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Subcategory(models.Model):
    SUBCATEGORY_NAME = (

        (CompanyName.CONST_STARTUP, CompanyName.CONST_STARTUP),
        (CompanyName.CONST_PROJECT_SUPPORT, CompanyName.CONST_PROJECT_SUPPORT),

        (CompanyName.CONST_WEB_STUDIO, CompanyName.CONST_WEB_STUDIO),
        (CompanyName.CONST_IT_COMPANY, CompanyName.CONST_IT_COMPANY),
        (CompanyName.CONST_B2G, CompanyName.CONST_B2G),

        (CompanyName.CONST_GAME_DEV, CompanyName.CONST_GAME_DEV),
        (CompanyName.IT_SAFETY, CompanyName.IT_SAFETY),
        (CompanyName.CONST_NONE_TYPE, CompanyName.CONST_NONE_TYPE)
    )
    subcategory_name = models.CharField('subcategory_name', max_length=100, choices=SUBCATEGORY_NAME)
    color = models.CharField('color', max_length=25, default="gray")
    description = models.TextField('description', default="")
    company_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING,  default='')

    def __str__(self):
        return self.subcategory_name

    # def save(self, *args, **kwargs):
    #     # match self.subcategory_name:
    #     #     case CompanyName.CONST_SELF_PRODUCT:
    #     #         self.style_name = 'self_product'
    #     #     case CompanyName.CONST_STARTUP:
    #     #         self.style_name = 'startup'
    #     #     case CompanyName.CONST_PROJECT_SUPPORT:
    #     #         self.style_name = 'project_support'
    #     #
    #     #     case CompanyName.CONST_CUSTOM_DEV:
    #     #         self.style_name = 'custom_dev'
    #     #     case CompanyName.CONST_WEB_STUDIO:
    #     #         self.style_name = 'web_studio'
    #     #     case CompanyName.CONST_IT_COMPANY:
    #     #         self.style_name = 'big_it_company'
    #     #     case CompanyName.CONST_B2G:
    #     #         self.style_name = 'b2g'
    #     #
    #     #     case CompanyName.CONST_GAME_DEV:
    #     #         self.style_name = 'game_dev'
    #     #     case CompanyName.CONST_NONE_TYPE:
    #     #         self.style_name = 'none_type'
    #     super(Subcategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'CompanySubcategory'
        verbose_name_plural = 'CompanySubcategories'


class Company(models.Model):
    name = models.CharField('name', max_length=150)
    logotype = models.ImageField('logotype', upload_to='companies/logo/img')
    short_description = models.TextField('short_description')
    url = models.CharField('url', max_length=200)
    accreditation = models.BooleanField('accreditation')
    phone = models.CharField('phone', max_length=200, null=True, blank=True)
    telegram = models.CharField('telegram', max_length=200, null=True, blank=True)
    email = models.CharField('email', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class CompanyCategory(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default='')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'CompanyCategory'
        verbose_name_plural = 'CompanyCategories'
        unique_together = ('subcategory', 'company')

    def __str__(self):
        return "\"%s\" принадлежит к %s" % (self.company, self.subcategory)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'company')

    def __str__(self):
        return "%s добавил в избранное %s" % (self.user, self.company)

class City(models.Model):
    name = models.CharField('name', max_length=150)
    coordinate_x = models.FloatField()
    coordinate_y = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

class Address(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, default='')
    street = models.CharField('street', max_length=150)
    home_number = models.CharField('home_number', max_length=15)
    coordinate_x = models.FloatField(blank=True, null=True)
    coordinate_y = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "%s %s %s" % (self.city, self.street, self.home_number)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def save(self, *args, **kwargs):
        if not self.coordinate_x or not self.coordinate_y:
            location = geocoder(f"{self.city} {self.street} {self.home_number}")

            if location:
                self.coordinate_x = location[0]
                self.coordinate_y = location[1]

        super().save(*args, **kwargs)

class CompanyAddress(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, default='')
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, default='')

    def __str__(self):
        return "%s располагается по адресу %s" % (self.company, self.address)

    class Meta:
        verbose_name = 'CompanyAddress'
        verbose_name_plural = 'CompanyAddresses'

class Tag(models.Model):
    name = models.CharField('street', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class CompanyTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING, default='')
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, default='')

    def __str__(self):
        return "%s имеет тег %s" % (self.company, self.tag)

    class Meta:
        verbose_name = 'CompanyTag'
        verbose_name_plural = 'CompanyTags'
