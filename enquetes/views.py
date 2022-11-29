from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import datetime

from .models import Question
from .forms import QuestionForm, QuestionModelForm, QuestionFormCustomTemplate, FormUser

# as views acima serão substituídas por views genéricas


# class IndexView (generic.ListView):
# template_name = 'index.html'  # nome do template
# nome do contexto que será passado para o template
#context_object_name = 'questions'
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


def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'index.html', context)


def details(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {'question': question}
    return render(request, 'details.html', context)


def create(request):

    if request.method == "POST":  # objeto do tipo dicionário
        #form = QuestionForm(request.POST)
        form = QuestionModelForm(request.POST)
        #form = QuestionFormCustomTemplate(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.pub_date = datetime.datetime.now()
            question.save()

            """ question = Question()
            question.question_text = form.cleaned_data['question_text']
            question.pub_date = datetime.datetime.now()
            question.save() """
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'create.html', {'form': form})
    else:
        #form = QuestionForm()
        #form = QuestionModelForm()
        form = QuestionFormCustomTemplate()
        return render(request, 'create.html', {'form': form})


def create_user(request):
    form = None
    if request.method == "POST":
        form = FormUser(request.POST)
        if form.is_valid():

            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            form = FormUser(request.POST)
    else:
        form = FormUser()

    return render(request, 'cadastrar_usuario.html', {'form': form})
