from django.db import models
from django.contrib.auth.models import User

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    answer = models.CharField(max_length=100)  # You can adjust this field as needed

class Member(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    id_number = models.CharField(max_length=100)
    
    def __str__(self):
        return(f"{self.id_number}")
    