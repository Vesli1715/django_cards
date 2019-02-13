from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required   # forbids access to unregistered user(used decorators)
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin   # forbids access to unregistered user in class based view


def index(request):
    count = User.objects.count()
    return render(request, 'registration/content.html', {'count': count })


def singup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('content.html')
    else:
        form = UserCreationForm()
    return render(request, 'registration/singup.html', {'form':form})


@login_required
def secret_page(request):
    return render(request, 'registration/secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'registration/secret_page.html'