from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm, NewsForm
from companies.models import Category, Subcategory, Company, City, Address, CompanyAddress, CompanyCategory, City
from internships.models import Internship
from .helpstructure import CategoryWithSubcategories, CompanyWithAddress
from .models import News


def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)  # Принимаем данные формы и файлы
        if form.is_valid():
            form.save()  # Сохраняем новость в базе данных
            return redirect('home')  # Перенаправляем на главную после успешного сохранения
    else:
        form = NewsForm()  # Пустая форма для GET-запроса
    return render(request, 'main/create_news.html', {'form': form})


def index(request):
    categories = Category.objects.all()
    categories_with_subcategories = []
    for category in categories:
        categor = CategoryWithSubcategories(category.id,
                                            category.category_name,
                                            category.color,
                                            category.description)
        categor.subcategories = Subcategory.objects.filter(company_category_id=category.id)
        categories_with_subcategories.append(categor)

    companies = Company.objects.all()

    # Получаем последние 5 новостей
    latest_news = News.objects.all().order_by('-created_at')[:5]

    context = {
        "categories": categories_with_subcategories,
        "companies_with_address": companies,
        "latest_news": latest_news  # Передаём новости в контекст
    }
    return render(request, 'main/index.html', context=context)


def map(request):
    subcategories = Subcategory.objects.all()
    companies = Company.objects.all()
    # Достаём город пользователя по его геолокации
    # city = City.objects.get(id=1)
    # result_companies = companies_to_companies_with_address(companies)

    context = {
        "subcategories": subcategories,
        # "city": city,
        "companies_with_address": companies
    }
    return render(request, 'main/map.html', context=context)


def companies_to_companies_with_address(companies):
    result_companies = []
    for comp in companies:
        company_categories = CompanyCategory.objects.filter(company_id=comp.id)
        subcategories_by_comp = [company_categoty.subcategory for company_categoty in company_categories]
        color = subcategories_by_comp[0].color
        comp_addresses_elems = CompanyAddress.objects.filter(company_id=comp.id)
        comp_addresses = [comp_addr_elem.address for comp_addr_elem in comp_addresses_elems]
        for address in comp_addresses:
            city = address.city
            address_name = "%s %s %s" % (city.name, address.street, address.home_number)
            company_with_address = CompanyWithAddress(comp.id, comp.name, color, address_name,
                                                      address.coordinate_x, address.coordinate_y)

            result_companies.append(company_with_address)
    return result_companies


def internship(request):
    internships = Internship.objects.all()

    return render(request, 'internships/internships_list.html', context={'internships': internships})


def get_object_or_404(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        raise Http404(f"{model._meta.verbose_name} не найден.")

def internship_detail(request, internship_id):
    # Получаем стажировку или возвращаем 404, если не найдена
    internship = get_object_or_404(Internship, pk=internship_id)

    # Рендерим шаблон с деталями стажировки
    return render(request, 'internships/internship_detail.html', {'internship': internship})