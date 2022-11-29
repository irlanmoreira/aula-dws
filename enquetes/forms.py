from django import forms
from .models import Question, User


def mobile_num(value):
    mobile = str(value)
    if len(mobile) != 10:
        raise forms.ValidationError("O número não pode ser menor que 10")


class QuestionForm(forms.Form):
    question_text = forms.CharField(
        label="Enquete", max_length=5)


class QuestionModelForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']


class QuestionFormCustomTemplate(forms.Form):
    question_text = forms.CharField(
        label="Enquete", max_length=100, min_length=5)
    template_name = 'forms/form_question.html'


class FormUser(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'gender': forms.RadioSelect(choices=User.GENDER)}
