from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InternshipCreationForm


@login_required
def create_internship(request):
    if request.method == 'POST':
        form = InternshipCreationForm(request.POST)
        if form.is_valid():
            internship = form.save(commit=False)
            internship.company = request.user  # Связываем стажировку с компанией (создателем)
            internship.save()
            return redirect('internship_list')  # Перенаправление на список стажировок
    else:
        form = InternshipCreationForm()

    return render(request, 'internships/create_internship.html', {'form': form})


def internship_list():
    return None