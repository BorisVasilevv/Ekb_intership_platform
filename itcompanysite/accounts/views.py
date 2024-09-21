from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.db.models import QuerySet
from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth import login
from companies.models import Company, Favorite, CompanyCategory
from django.utils.http import urlsafe_base64_decode
from django.views import View
from .forms import MyAuthenticationForm, CompanyCreationForm, StudentCreationForm, EducationCreationForm
from .utils import send_email_for_verify
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from .helpstructure import CompanyWithCategoryData
from django.http import Http404

User = get_user_model()


def registration(request):
    if request.method == 'POST':
        user_type = request.POST.get('role')

        if user_type == 'company':
            user_reg_form = CompanyCreationForm(request.POST)
        elif user_type == 'educational_institution':
            user_reg_form = EducationCreationForm(request.POST)
        else:
            user_reg_form = StudentCreationForm(request.POST)

        if user_reg_form.is_valid():
            # Установите роль здесь
            user_reg_form.cleaned_data['role'] = user_type

            # Присваиваем роль перед сохранением
            user = user_reg_form.save(commit=True)  # Теперь сохранение вызовет создание других объектов
            send_email_for_verify(request, user)
            return redirect('/accounts/confirm_email/')
        else:
            print(user_reg_form.errors)  # Логируем ошибки для диагностики

        return render(request, 'accounts/registration.html', {'user_form': user_reg_form, 'role': user_type})

    roles = [role[0] for role in User.ROLE_CHOICES if role[0] != 'admin']
    return render(request, 'accounts/chosen_role_reg.html', {'roles': roles})


def profile(request):
    user = request.user
    favorite_entries = Favorite.objects.filter(user_id=user.id)
    companies_for_user = [entry.company for entry in favorite_entries]
    result_companies = []
    
    for comp in companies_for_user:
        company_categories = CompanyCategory.objects.filter(company_id=comp.id)
        subcategories_by_comp = [company_categoty.subcategory for company_categoty in company_categories]
        categories_by_comp = [subcat.company_category for subcat in subcategories_by_comp]
        result_companies.append(CompanyWithCategoryData(comp.id, comp.name, comp.logotype, comp.short_description,
                                                        comp.url, categories_by_comp, subcategories_by_comp,
                                                        comp.phone, comp.telegram, comp.accreditation, comp.email))
    
    if user.is_student():
        return render(request, 'accounts/profile.html', {'companies': result_companies})
    elif user.is_admin():
        return render(request, 'accounts/profile_admin.html', {'companies': result_companies})
    elif user.is_company():
        return render(request, 'accounts/profile_company.html', {'companies': result_companies})
    elif user.is_educational_institution():
        return render(request, 'accounts/profile_educational_institution.html', {'companies': result_companies})
    else:
        raise Http404("User type not recognized")


class EmailView(View):
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)
        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('profile')
        return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
                TypeError,
                ValueError,
                OverflowError,
                User.DoesNotExist,
                ValidationError,
        ):
            user = None
        return user


@csrf_protect
@require_POST
def remove_from_favorites(request, company_id):
    if request.user.is_authenticated:
        try:
            company = Company.objects.get(id=company_id)
            favorite = Favorite.objects.get(user=request.user, company=company)
            favorite.delete()
            return JsonResponse({'status': 'success'})
        except (Company.DoesNotExist, Favorite.DoesNotExist):
            return JsonResponse({'status': 'error', 'message': 'Компания не найдена в избранном пользователя.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Пользователь не аутентифицирован.'})


class MyLoginView(LoginView):
    template_name = "accounts/login.html"
    form_class = MyAuthenticationForm
