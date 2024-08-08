#users/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Создаем здесь представления. 

def home(request):
    return render(request,"users/home.html")



class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Переадресация на главную страницу после успешной регистрации
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
