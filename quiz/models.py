from django.db import models

# Question Model

class Question(models.Model):
    text = models.TextField()
    option1 = models.CharField(max_length=300)
    option2 = models.CharField(max_length=300)
    option3 = models.CharField(max_length=300)
    option4 = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=300)

    def _str__(self):
        return self.text
    
class UserSession(models.Model):
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)

    def _str__(self):
        return f"Session {self.id}"

