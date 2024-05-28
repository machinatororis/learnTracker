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


def topic(reguest, topic_id):  # в topic_id зберігаємо вираз з <int:topic_id>
    """Показує одну тему та всі її записи"""
    topic = Topic.objects.get(id=topic_id)  # отримуємо тему
    entries = topic.entry_set.order_by(
        "-date_added"
    )  # завантажуємо записи, впорядковуємо у зворотньому порядку
    context = {
        "topic": topic,
        "entries": entries,
    }  # зберігаємо тему і записи у контекст, який передамо потім шаблону
    return render(reguest, "learn_trackers/topic.html", context)
