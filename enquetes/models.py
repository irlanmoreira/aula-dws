from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(
        max_length=10, verbose_name='Título da enquete')
    pub_date = models.DateTimeField('Data de publicação')

    def __str__(self):
        return self.question_text
