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
    restaurant = models.ForeignKey(
        Course, related_name='content', on_delete=models.CASCADE)
    week_id = models.CharField(max_length=20)

    class Meta:
        db_table = "content"

    def __str__(self):
        return self.week_id


class Day(models.Model):
    week = models.ForeignKey(
        Content, related_name='day', on_delete=models.CASCADE)
    week_count = models.CharField(max_length=20, default="week count")
    day1 = models.CharField(max_length=256, default='day 1 content')
    day2 = models.CharField(max_length=256, default='day 2 content')
    day3 = models.CharField(max_length=256, default='day 3 content')
    day4 = models.CharField(max_length=256, default='day 4 content')
    day5 = models.CharField(max_length=256, default='day 5 content')

    class Meta:
        db_table = "days"

    def __str__(self):
        return self.week_count
