from django.shortcuts import render
from django.views.generic.list import ListView # smth new. https://www.dennisivy.com/post/django-class-based-views/ this maybe
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Taskai

# Create your views here.

class TaskaiList(ListView):
    model = Taskai
    context_object_name = 'taskiukai' # call this kaip nori, so instead of "object list in html template I can use "taskai""

class TaskaiDetail(DetailView):
    model = Taskai
    context_object_name = 'taskas'

class TaskaiCreate(CreateView):
    model = Taskai
    fields = '__all__'
    # field = ['title', 'description'] # one way to do it or list all like above
    success_url = reverse_lazy('visi-taskai')

class TaskaiUpdate(UpdateView):
    model = Taskai
    fields = '__all__'
    success_url = reverse_lazy('visi-taskai')

class DeleteView(DeleteView):
     model = Taskai
     context_object_name = 'raganosis'
     success_url = reverse_lazy('visi-taskai')
