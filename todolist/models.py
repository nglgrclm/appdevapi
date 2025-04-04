from django.db import models

# Create your models here.

class ToDo(models.Model):
    name = models.CharField(max_length=255, verbose_name="Task Name")
    details = models.TextField(blank=True, verbose_name="Task Details")
    completed = models.BooleanField(default=False, verbose_name="Completed")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name