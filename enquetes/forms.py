from django import forms
from .models import Question, Choice


class QuestionForm(forms.Form):
    question_text = forms.CharField(
        label='Enquete', max_length=30, min_length=5)


class QuestionModelForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']


class ChoiceModelForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']


class VoteForm(forms.Form):

    choices = forms.ChoiceField(
        widget=forms.RadioSelect(), label="Opções")

    def __init__(self, *args, **kwargs):
        self.question_id = kwargs.pop('question_id')

        super(VoteForm, self).__init__(*args, **kwargs)

        question = Question.objects.get(pk=self.question_id)
        choices = question.choice_set.all()
        self.fields['choices'].choices = (
            [(c.id, c.choice_text) for c in choices])
