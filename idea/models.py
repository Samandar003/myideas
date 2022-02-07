from django.urls import reverse, reverse_lazy
from pyexpat import model
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from datetime import date
from django.utils import timezone
User = get_user_model()


class Idea(models.Model):
  
  IDEA_CHOICES = [
    ('Social', 'Social'),
    ('Educational', 'Educational'),
    ('IT', 'IT'),
    ('Law', 'Law'),
    ('Personal', 'Personal'),
    ('Metal', 'Mental'),
    ('Environmental', 'Environmental'),
    ('Economical', 'Economical'),
    ('Health', 'Health'),
    ('Other', 'Other')
  ]

  title = models.CharField(max_length=100)
  related = models.CharField(max_length=100, choices=IDEA_CHOICES, default='Other')
  content = models.TextField(blank=True, null=False)
  date_posted = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  def get_absolute_url(self):
      return reverse_lazy('ideas')

  def __str__(self):
      return self.title
  class Meta:
    ordering = ['-date_posted']
    
