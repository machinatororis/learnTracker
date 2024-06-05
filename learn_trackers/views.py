from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm


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


def new_entry(
    request, topic_id
):  # містить topic_id для зберігання отриманого значення з URL
    """Додає новий запис по конкретній темі"""
    topic = Topic.objects.get(
        id=topic_id
    )  # використовуємо topic_id для отримання об'єкта теми
    if request.method != "POST":
        # Дані не відправлялись, створюємо порожню форму
        form = EntryForm()
    else:
        # Відправлені дані POST, оброблюємо дані
        form = EntryForm(
            data=request.POST
        )  # створюємо EntryForm, заповнений даними POST з об'єкту request
        if form.is_valid():
            new_entry = form.save(
                commit=False
            )  # зберігаємо новий запис у new_entry, без запису у БД
            new_entry.topic = topic  # додаємо запису його тему
            new_entry.save()  # зберігаємо в БД з правильно зв'язанною темою
            return redirect(
                "learn_trackers:topic", topic_id=topic_id
            )  # редірект на тему, для якої бул доданий запис

    # Виводимо порожню або недійсну форму
    context = {"topic": topic, "form": form}
    return render(request, "learn_trackers/new_entry.html", context)
