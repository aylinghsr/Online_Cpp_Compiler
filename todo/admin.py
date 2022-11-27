from django.contrib import admin
from .models import todo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ()

admin.site.register(todo, TodoAdmin)
