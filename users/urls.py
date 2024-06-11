"""Визначає схеми URL для користувачів"""

from django.urls import path, include

app_name = "users"
urlpatterns = [
    # ввімкнути URL авторизації за замовченням
    path("", include("django.contrib.auth.urls")),
]
