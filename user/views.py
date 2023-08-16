from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Log in!')
            return redirect('login')
    else:
        form = UserForm()       

    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request) : 
    return render(request, 'user/profile.html')