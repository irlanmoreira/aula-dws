from django import forms
from .models import Question


class QuestionForm(forms.Form):
    question_text = forms.CharField(
        label='Enquete', max_length=30, min_length=5)


class QuestionModelForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
