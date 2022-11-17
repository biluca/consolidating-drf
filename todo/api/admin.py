from django.contrib.admin import site
from django.contrib.admin import ModelAdmin
from api.models import Todo


class TodoAdmin(ModelAdmin):
    list_display = ("name", "done", "created_at")
    list_filter = ["name"]


site.register(Todo, TodoAdmin)
