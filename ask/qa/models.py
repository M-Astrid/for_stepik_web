from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Model):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()

    title = models.CharField(max_length=255)
    text = models.TextField
    added_at = models.DateField(blank = True, auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/question/%d/' % self.pk

class Answer(models.Model):

    text = models.TextField
    added_at = models.DateField(blank = True, auto_now_add=True)
    question = ForignKeyField('Question')
    author = models.ForiegnKeyField(User)