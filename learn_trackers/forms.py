from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic  # кажемо django, на якій моделі буде базуватися форма
        fields = ["text"]  # кажемо django, які поля будуть на формі
        labels = {"text": ""}  # кажемо не генерувати підпис для text field


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": "Entry:"}
        widgets = {
            "text": forms.Textarea(attrs={"cols": 80})
        }  # віджет вводу, ширина 80 замість стандартних 40
