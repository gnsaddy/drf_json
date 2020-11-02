from django.db import models
from django.db.models.base import Model

class Course(models.Model):
    title = models.CharField(max_length=250)
    subContent = models.CharField(max_length=1000)
    duration = models.CharField(max_length=250)
    price = models.IntegerField()
    coordinator = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "course"

    def __str__(self):
        return self.title


class Content(models.Model):
    restaurant = models.ForeignKey(Course, on_delete=models.CASCADE)
    week_id = models.CharField(max_length=20)

    class Meta:
        db_table = "content"

    def __str__(self):
        return self.week_id

