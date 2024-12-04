from django.db import models
from colorfield.fields import ColorField


# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=100)
    color = ColorField(default='#7BB7EC')
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):
        return self.title