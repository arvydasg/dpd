from django.shortcuts import render
from django.views.generic.list import ListView # smth new. https://www.dennisivy.com/post/django-class-based-views/ this maybe
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin # and add LoginRequiredMixin to TaskaiList skliaustelius

from . models import Taskai

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'          # no need of separate form html, it's already created
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('visi-taskai')

class TaskaiList(LoginRequiredMixin, ListView):
    model = Taskai
    context_object_name = 'taskiukai' # call this kaip nori, so instead of "object list in html template I can use "taskai""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taskiukai'] = context['taskiukai'].filter(user=self.request.user)
        # context['count'] = context['taskiukai'].filter(complete=False).count() # no need this for me, not a todo app
        return context

class TaskaiDetail(LoginRequiredMixin, DetailView):
    model = Taskai
    context_object_name = 'taskas'

class TaskaiCreate(LoginRequiredMixin, CreateView):
    model = Taskai
    fields = '__all__'
    # field = ['title', 'description'] # one way to do it or list all like above
    success_url = reverse_lazy('visi-taskai')

class TaskaiUpdate(LoginRequiredMixin, UpdateView):
    model = Taskai
    fields = '__all__'
    success_url = reverse_lazy('visi-taskai')

class DeleteView(LoginRequiredMixin, DeleteView):
     model = Taskai
     context_object_name = 'raganosis'
     success_url = reverse_lazy('visi-taskai')
