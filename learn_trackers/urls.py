"""Визначає схеми URL для learn_trackers"""

from django.urls import path  # необхідна для зв'язування URL з представленнями
from . import (
    views,
)  # .  - імпортує з каталога, в якому знаходиться поточний модуль urls.py

app_name = "learn_trackers"  # за допомогою app_name відрізняємо різні urls.py між собою
urlpatterns = [  # список сторінок, які можуть запитуватися з застосунку learn_trackers
    # Домашня сторінка
    path("", views.index, name="index"),  # схема URL
    # Сторінка зі списком всіх тем
    path("topics/", views.topics, name="topics"),
    # Сторінка з детальною інформацією по окремій темі
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    # Сторінка для додавання нової теми
    path("new_topic/", views.new_topic, name="new_topic"),
    # Сторінка для додавання нових записів
    # <int:topic_id> числове значення теми, яке зберігається в topic_id
    path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),
    # Сторінка для редагування записів
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
]
