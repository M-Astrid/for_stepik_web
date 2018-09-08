from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Question, Answer
from .forms import AskForm, AnswerForm, SignUpForm

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "signup.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    args = {}
    args['form'] = form
    return render(request, 'signup.html', args)


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