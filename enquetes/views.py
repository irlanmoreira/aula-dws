from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}

    return render(request, 'index.html', context)
# Create your views here.


def details(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'details.html', {'question': question})
