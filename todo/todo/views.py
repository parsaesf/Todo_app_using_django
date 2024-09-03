from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from todo import models
from todo.models import TODOO
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)

from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import *
from .forms import TodoForm


class IndexView(TemplateView):
    template_name = "todo/signup.html"


# @login_required(login_url='/loginn')
# def home(request):
#     return render(request, 'signup.html')


def signup(request):
    if request.method == "POST":
        fnm = request.POST.get("fnm")
        emailid = request.POST.get("emailid")
        pwd = request.POST.get("pwd")
        print(fnm, emailid, pwd)
        my_user = User.objects.create_user(fnm, emailid, pwd)
        my_user.save()
        return redirect("/loginn")

    return render(request, "todo/signup.html")


def loginn(request):
    if request.method == "POST":
        fnm = request.POST.get("fnm")
        pwd = request.POST.get("pwd")
        print(fnm, pwd)
        userr = authenticate(request, username=fnm, password=pwd)
        if userr is not None:
            login(request, userr)
            return redirect("/todo/")
        else:
            return redirect("/loginn")

    return render(request, "todo/loginn.html")


class TodoListView(LoginRequiredMixin, ListView):
    model = TODOO
    template_name = "todo/todo_list.html"
    context_object_name = "res"


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = TODOO

    def get_success_url(self):
        return reverse("todo-list")


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = TODOO
    form_class = TodoForm

    def get_success_url(self):
        return reverse("todo-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoEditView(LoginRequiredMixin, UpdateView):
    model = TODOO
    form_class = TodoForm

    def get_success_url(self):
        return reverse("todo-list")


def signout(request):
    logout(request)
    return redirect("/loginn")
