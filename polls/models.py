import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Model to creata"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('ending date', default=timezone.now() + datetime.timedelta(days=10))

    def __str__(self):
        return self.question_text

    def is_published(self):
        return timezone.now() >= self.pub_date

    def can_vote(self):
        return self.end_date > timezone.now() >= self.pub_date

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text