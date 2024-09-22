from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InternshipCreationForm
from .models import Internship, StudentResponseFile
from django.http import Http404
from accounts.forms import StudentResponseForm


def get_object_or_404(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        raise Http404(f"{model._meta.verbose_name} не найден.")


def create_internship(request):
    if request.method == 'POST':
        form = InternshipCreationForm(request.POST)
        if form.is_valid():
            internship = form.save()
            internships = Internship.objects.all()
            return render(request, 'internships/internships_list.html', {'internships': internships})
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


def create_student_response(request, internship_id):
    internship = Internship.objects.get(id=internship_id)

    if request.method == "POST":
        form = StudentResponseForm(request.POST)
        if form.is_valid():
            student_response = form.save(commit=False)
            student_response.student = request.user
            student_response.internship = internship
            student_response.save()

            # Сохранение файлов
            selected_files = form.cleaned_data['files']
            for file in selected_files:
                StudentResponseFile.objects.create(response=student_response, file=file)

            return redirect('internship_detail', internship_id=internship.id)
    else:
        form = StudentResponseForm()

    return render(request, 'internships/internship_response.html', {'form': form, 'internship': internship})
