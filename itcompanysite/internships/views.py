from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InternshipCreationForm
from .models import Internship
from django.http import Http404


def get_object_or_404(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        raise Http404(f"{model._meta.verbose_name} не найден.")


@login_required
def create_internship(request):
    if request.method == 'POST':
        form = InternshipCreationForm(request.POST)
        if form.is_valid():
            internship = form.save()
            return redirect('internships_list')
    else:
        form = InternshipCreationForm()

    return render(request, 'internships/create_internship.html', {'form': form})


def internships_list(request):
    internships = Internship.objects.all()
    return render(request, 'internships/internships_list.html', {'internships': internships})


def internship_detail(request, internship_id):
    # Получаем стажировку или возвращаем 404, если не найдена
    internship = get_object_or_404(Internship, pk=internship_id)

    # Рендерим шаблон с деталями стажировки
    return render(request, 'internships/internship_detail.html', {'internship': internship})

