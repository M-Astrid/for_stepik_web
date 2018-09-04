from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Question


def main(request):
    questions = Question.objects.all().order_by('-id')
    paginator = Paginator(questions, 10)
    try:
        page = request.GET.get('page', 1)
    except ValueError:
        page = 1
    except TypeError:
        page = 1

    try:
        page = paginator.page(page)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'main.html', {'title':'main.html',
                                         'paginator':paginator,
                                         'questions':page.object_list,
                                         'page': page, })


def popular(request):
    questions = Question.objects.all().order_by('-rating')
    paginator = Paginator(questions, 10)
    try:
        page = request.GET.get('page', 1)
    except ValueError:
        page = 1
    except TypeError:
        page = 1

    try:
        page = paginator.page(page)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'main.html', {'title': 'main.html',
                                         'paginator': paginator,
                                         'questions': page.object_list,
                                         'page': page, })

def question(request, num,):
    try:
        q = Question.objects.get(id=num)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'question.html', {'question': q, })

def test(request, *args, **kwargs):
    return HttpResponse("OK %s" % kwargs["num"])
