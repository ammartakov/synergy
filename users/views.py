from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserName
from .forms import UserNameForm

def index(request):
    # Получаем все имена из базы данных
    all_names = UserName.objects.all()
    
    # Переменная для последнего приветствия
    greeting = None
    
    if request.method == 'POST':
        form = UserNameForm(request.POST)
        if form.is_valid():
            # Сохраняем имя в базу данных
            user_name = form.save()
            greeting = f"Привет, {user_name.name}!"
            messages.success(request, f"Добро пожаловать, {user_name.name}!")
            # Перенаправляем чтобы избежать повторной отправки формы
            return redirect('index')
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = UserNameForm()
    
    context = {
        'form': form,
        'greeting': greeting,
        'all_names': all_names,
    }
    return render(request, 'users/index.html', context)