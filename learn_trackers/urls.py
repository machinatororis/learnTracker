"""Визначає схеми URL для learn_trackers"""

from django.urls import path  # необхідна для зв'язування URL з представленнями
from . import views  # .  - імпортує з каталога, в якому знаходиться поточний модуль urls.py

app_name = "learn_trackers"  # за допомогою app_name відрізняємо різні urls.py між собою
urlpatterns = [  # список сторінок, які можуть запитуватися з застосунку learn_trackers
    # Домашня сторінка
    path("", views.index, name="index"),  # схема URL
]
