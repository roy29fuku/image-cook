from django.db import models
from datetime import datetime

class Book(models.Model):
    class Meta:
        db_table = 'books'
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title

