from django.contrib import admin
from .models import ToDo

@admin.register(ToDo)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'completed', 'created_at', 'updated_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('name', 'details')