from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255)
    due_date = models.DateTimeField(null=True, blank=True)  # Optional
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
