from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Реєстрація нового користувача"""
    # Перевіряємо, чи відповідає ф-ція на запит POST
    if request.method != "POST":
        # Показуємо порожню форму реєстрації
        form = UserCreationForm()
    else:
        # Обробка заповненної форми
        # Створюємо екземпляр класу UserCreationForm на основі відправлених даних
        form = UserCreationForm(data=request.POST)

        # Перевіряємо, чи вірні дані
        if form.is_valid():
            new_user = form.save()  # зберігаємо ім'я користувача і хеш пароля в БД
            # Виконання входу і перенаправлення на домашню сторінку
            login(request, new_user)
            return redirect("learn_trackers:index")

    # Показуємо порожню або недійсну форму
    context = {"form": form}
    return render(request, "registration/register.html", context)
