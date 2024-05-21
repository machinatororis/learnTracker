from django.contrib import admin
from .models import Topic

# реєструємо модель з імпорту, керування моделлю буде з адміністративного сайту
admin.site.register(Topic)
