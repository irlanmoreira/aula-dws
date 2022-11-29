from email.policy import default
from django.db import models


# Create your models here.


class Question(models.Model):
    question_text = models.CharField("Enquete", max_length=100)
    pub_date = models.DateTimeField(
        'Data de publicação', auto_now_add=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        self.choice_text


class User(models.Model):
    GENDER = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    name = models.CharField("Nome", max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER)
