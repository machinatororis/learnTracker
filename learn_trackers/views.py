from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm


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


def new_topic(request):
    """Визначає нову тему"""
    # перевіряємо, був запит GET чи POST
    if request.method != "POST":
        # Дані не відправлялись, створюємо порожню форму
        form = TopicForm()
    else:
        # Відправлені дані POST, оброблюємо дані
        form = TopicForm(data=request.POST)
        if (
            form.is_valid()
        ):  # перевіряємо, чи всі обов'язкові поля заповнені, тоді зберігаємо в БД
            form.save()
            return redirect("learn_trackers:topics")

    # Виводимо порожню або недійсну форму
    context = {"form": form}
    return render(request, "learn_trackers/new_topic.html", context)
