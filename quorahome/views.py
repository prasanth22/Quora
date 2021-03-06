from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
import datetime
# Create your views here.

def home(request):
    form = QuestionForm(request.POST or None)
    print (request.POST)
    context = {
        "form": form
    }
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
    return render(request, 'quorahome.html', context)

def questions(request):
    questions = Question.objects.all()
    context = { 'questions' : questions}
    return render(request, 'questions.html', context)

def viewquestion(request, pk):
    questions = get_object_or_404(Question, pk=pk)
    answers = Answer.objects.all()
    context = {
        'questions':questions,
        'answers':answers
    }
    return render(request, 'viewquestion.html', context)

def current_time(request):
    now = datetime.datetime.now()
    html = "<html> <body> It is now %s </body> </html>" %now
    return HttpResponse(html)
