from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse
from django.views import View

from .forms import UserForm
from .models import User


class UserListView(ListView):
    model = User
    form_class = UserForm
    template_name = 'users/users_list.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/create.html'
    context_object_name = 'users'
    success_url = reverse_lazy('users_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить клиента'
        context['button_name'] = 'Сохранить клиента'
        return context


def index(request):
    # return HttpResponse("This is index text")
    context = {
        'name': 'Myrza',
        'age': 25
    }
    return render(request, 'index.html', context)


class Index(View):
    def get(self, request, *args, **kwargs):
        context = {
            'name': 'Myrza',
            'age': 25
        }
        return render(request, 'index.html', context)


# def create_user(request):
#     if request.method == "GET":
#         return render(request, 'users/create_user.html')
#     if request.method == "POST":
#         name = request.POST.get("name")
#         age = request.POST.get("age")
#         place_of_birth = request.POST.get("place_of_birth")
#         User.objects.create(name=name, age=age, place_of_birth=place_of_birth)
#         return HttpResponseRedirect(reverse('users_list'))


def create_user(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users_list'))
    context = {
        'form': form
    }
    return render(request, 'users/create_user.html', context)


class CreateUser(View):
    form = UserForm
    template_name = 'users/create_user.html'
    success_url = 'users_list'

    def get_context_data(self, **kwargs):
        form = self.form()
        context = {
            'form': form
        }
        return context

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(self.success_url))
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
