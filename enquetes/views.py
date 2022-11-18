from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from .forms import QuestionForm, QuestionModelForm
import datetime


def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}

    return render(request, 'index.html', context)
# Create your views here.


def details(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'details.html', {'question': question})


def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            question = Question()
            question.question_text = form.cleaned_data['question_text']
            question.pub_date = datetime.datetime.now()
            question.save()
            return redirect('index')
        else:
            return render(request, 'create.html', {'form': form})

    else:
        form = QuestionForm()
        return render(request, 'create.html', {'form': form})
