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
        return self.choice_text

    def vote(self):
        self.votes = self.votes + 1


class User(models.Model):
    GENDER = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    name = models.CharField("Nome", max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER)


class Address(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}, {self.address.name}"


class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline
