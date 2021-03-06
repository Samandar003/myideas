from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


class CustomLoginView(LoginView):  
  template_name = 'user/login.html'
  fields = '__all__'
  redirect_authenticated_user = True
  def get_success_url(self) -> str:
      return reverse_lazy('ideas')  


def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f"Account created for {username}")
      return redirect('login')
  else:
    form = UserRegisterForm()
  return render(request, 'user/register.html', {'form':form})

@login_required
def profile(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST,
                               request.FILES, 
                               instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request, 'Your account has been updated')
      redirect('profile') 
  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
      
  context = {
    'u_form': u_form,
    'p_form': p_form
  }

  return render(request, 'user/profile.html', context)


