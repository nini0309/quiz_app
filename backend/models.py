from django.db import models

# Create your models here.
class Question(models.Model):
    type = models.CharField(max_length=50, blank = True, null = True)
    category = models.CharField(max_length=100, blank = True, null = True)
    difficulty = models.CharField(max_length=100, blank = True, null = True)
    question = models.CharField(max_length=500, blank = True, null = True)
    correct = models.CharField(max_length=50, blank = True, null = True)
    wrong = models.CharField(max_length=500, blank = True, null = True)

    def __str__(self):
        return self.question
