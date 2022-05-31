from django.db import models

# Create your models here.

class Todo(models.Model):
    item = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)