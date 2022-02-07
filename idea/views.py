from email import message
from django.shortcuts import redirect, render
from .models import Idea
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



class IdeaListView(LoginRequiredMixin, ListView):
  model = Idea
  context_object_name = 'ideas'
  template_name = 'idea/idea_list.html'
  redirect_authenticated_user = True

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['ideas'] = Idea.objects.all()
      context['count'] = context['ideas'].filter(author=self.request.user).count()
      return context
    

class IdeaDetailView(DetailView):
  model = Idea
  fields = ['title', 'realted', 'content', 'author']
  template_name = 'idea/idea_detail.html'
  
class IdeaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Idea
  fields = ['title', 'related', 'content']
  template_name = 'idea/idea_update.html'
  def form_valid(self, form):
      form.instance.author = self.request.user
      return super(IdeaUpdateView, self).form_valid(form)
  def test_func(self):
    idea = self.get_object()
    if idea.author == self.request.user:
      return True
    return False

  
class IdeaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Idea
  context_object_name = 'idea'
  template_name = 'idea/idea_delete_confirm.html'
  success_url = reverse_lazy('ideas')
  def test_func(self):
      idea = self.get_object()
      if idea.author == self.request.user:
        return True
      return False
  
class IdeaCreateView(LoginRequiredMixin, CreateView):
  model = Idea
  fields = ['title', 'related', 'content']
  template_name = 'idea/idea_create.html'
  def form_valid(self, form):
      form.instance.author = self.request.user
      return super(IdeaCreateView, self).form_valid(form)
    
    
    