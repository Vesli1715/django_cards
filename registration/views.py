from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
def index(request):
    count = User.objects.count()
    return render(request,'registration/content.html',{'count': count })

def singup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('content.html')
    else:
        form = UserCreationForm()
    return render(request, 'registration/singup.html',{'form':form})
