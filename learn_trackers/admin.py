from django.contrib import admin
from .models import Topic
from .models import Entry

# реєструємо модель з імпорту, керування моделлю буде з адміністративного сайту
admin.site.register(Topic)
admin.site.register(Entry)
