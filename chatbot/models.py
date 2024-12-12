from django.db import models

# Create your models here.
class Chat(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Q: {self.question} | A: {self.answer}"    