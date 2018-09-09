from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, LoginForm, SignupForm

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(username, password)
            user = authenticate(username=username, password=password)
            print(type(user))
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form,
                                          'user': request.user,
                                          'session': request.session, })


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data["username"]
            password = form.raw_passeord
            user = authenticate(username=username, password=password)
            print(type(user))
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form,
                                           'user': request.user,
'session': request.session, })


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

def new(request):
    questions = Question.objects.all().order_by('-added_at')
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
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            answer = form.save()
            url = q.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question':q.id})

    return render(request, 'question.html', {'question': q,
                                             'form': form, })

def go_ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'go_ask.html', {'form': form})