from django.db import models
from django.utils import timezone
import datetime

class Problem(models.Model):
    problem_text = models.CharField(max_length = 200)
    description_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    successful_rate = models.IntegerField(default = 0);
    solution = models.CharField(max_length=500)
    test_cases = models.CharField(max_length=500)
    tag_text = models.CharField(max_length= 200)
    difficulty = models.IntegerField(default = 0)
    def __str__(self):
        return self.problem_text;

# Create your models here.
