from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Тема, яку вивчає користувач"""

    text = models.CharField(max_length=200)
    # при додаванні нової теми, використовуємо теперішню дату
    date_added = models.DateTimeField(
        auto_now_add=True
    )  # блок для зберігання дати та часу
    # якщо користувач видаляється, всі його теми теж видаляються
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


def __str__(self):
    """Повертає рядкове представлення моделі (повертає рядок, який зберігається в атрибуті text)"""
    return self.text


class Entry(models.Model):
    """Записи користувача по обраній ним темі"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # on_delete=models.CASCADE - при видаленні теми всі записи цієї теми також видаляться. Каскадне видалення

    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"  # перевизначаємо множину для Entry: Entries замість стандартної Entrys

    def __str__(self):
        if len(self.text) > 50:
            """Повертає рядкове представлення моделі"""
            return f"{self.text[:50]}..."
            # показуємо лише перші 50 символів у рядку та додаємо ... для розуміння, що це не повний запис
        else:
            return f"{self.text}"
