from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import datetime

from .models import Question, Choice
from .forms import QuestionForm, QuestionModelForm, QuestionFormCustomTemplate, ChoiceModelForm, VoteForm


def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'index.html', context)


def details(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {'question': question}
    return render(request, 'details.html', context)


def create(request):
    form_question = QuestionModelForm()
    form_choice1 = ChoiceModelForm(prefix='choice1')
    form_choice2 = ChoiceModelForm(prefix='choice2')
    question = Question.objects.get(pk=1)
    print(question.choice_set.all())
    if request.method == 'POST':
        form_question = QuestionModelForm(request.POST)
        form_choice1 = ChoiceModelForm(request.POST, prefix='choice1')
        form_choice2 = ChoiceModelForm(request.POST, prefix='choice2')

        if all([form_question.is_valid(), form_choice1.is_valid(), form_choice2.is_valid()]):
            question = form_question.save()
            choice1 = form_choice1.save(commit=False)
            choice2 = form_choice2.save(commit=False)
            choice1.question = choice2.question = question
            choice1.save()
            choice2.save()
            return redirect('index')
    context = {'form_question': form_question,
               'form_choice1': form_choice1, 'form_choice2': form_choice2}
    return render(request, 'create.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    form = VoteForm(question_id=question_id)

    context = {'question': question, 'form': form}
    if request.method == "POST":
        form = VoteForm(request.POST, question_id=question_id)

        if form.is_valid():
            choice = Choice.objects.get(pk=form.cleaned_data['choices'])
            choice.vote()
            return redirect('index')
    return render(request, 'vote.html', context)

# as views acima serão substituídas por views genéricas


# class IndexView (generic.ListView):
# template_name = 'index.html'  # nome do template
# nome do contexto que será passado para o template
# context_object_name = 'questions'
""" model = Question """

""" def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.all()
        return context """

# def get_queryset(self):
#    return Question.objects.all()


""" class DetailView (generic.DetailView):
    model = Question
    template_name = 'details.html' """
