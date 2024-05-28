from django.shortcuts import render
from .models import Topic


def index(reguest):
    """Домашня сторінка застосунку learnTracker"""
    return render(reguest, "learn_trackers/index.html")


def topics(reguest):
    """Показує список тем"""
    topics = Topic.objects.order_by(
        "date_added"
    )  # Питаємо в БД об'єкти Topic відсортовані по атрибуту date_added
    context = {
        "topics": topics
    }  # Передаємо в шаблон пари ключ-значення, які містять набори тем
    return render(reguest, "learn_trackers/topics.html", context)
