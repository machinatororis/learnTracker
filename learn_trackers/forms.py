from django import forms

from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic  # кажемо django, на якій моделі буде базуватися форма
        fields = ["text"]  # кажемо django, які поля будуть на формі
        labels = {"text": ""}  # кажемо не генерувати підпис для text field
