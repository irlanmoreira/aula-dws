from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Question(models.Model):
    question_text = models.CharField("Enquete", max_length=100)
    Author = models.ForeignKey(
        get_user_model(), verbose_name="Autor", on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(
        'Data de publicação', auto_now_add=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name="Opção")
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def vote(self):
        self.votes = self.votes + 1
        self.save()
