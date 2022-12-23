from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Question, Choice
from .forms import QuestionModelForm, ChoiceModelForm, VoteForm


@login_required(login_url='/user/login')
def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'index.html', context)


class IndexView (LoginRequiredMixin, ListView):
    template_name = "index.html"
    model = Question
    context_object_name = "questions"
    login_url = '/user/login'


class DetailsQuestionView (LoginRequiredMixin, DetailView):
    template_name = "details.html"
    model = Question
    login_url = '/user/login'

    def get_object(self):
        self.question = get_object_or_404(Question, pk=self.kwargs['pk'])
        return self.question


def details(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {'question': question}
    return render(request, 'details.html', context)


class CreateQuestionView(LoginRequiredMixin, CreateView):
    login_url = '/user/login'
    model = Question
    form_class = ""


@login_required(login_url='/user/login')
def create(request):
    form_question = QuestionModelForm()
    form_choice1 = ChoiceModelForm(prefix='choice1')
    form_choice2 = ChoiceModelForm(prefix='choice2')
    question = None

    if request.method == 'POST':
        form_question = QuestionModelForm(request.POST)
        form_choice1 = ChoiceModelForm(request.POST, prefix='choice1')
        form_choice2 = ChoiceModelForm(request.POST, prefix='choice2')

        if all([form_question.is_valid(), form_choice1.is_valid(), form_choice2.is_valid()]):
            autor = request.user

            question = form_question.save(commit=False)
            question.Author = autor
            question.save()
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
            messages.success(request, "Voto computado com sucesso!")

            return redirect('index')
    return render(request, 'vote.html', context)
