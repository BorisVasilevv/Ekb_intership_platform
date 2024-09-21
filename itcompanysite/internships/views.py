from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InternshipCreationForm
from .models import Internship


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

