from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib.auth.models import Group
from .forms import RegisterForm, LoginForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)


class IndexView(LoginRequiredMixin, TemplateView):
   template_name = 'protect/index.html'

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['is_not_author'] = not self.request.user.groups.filter(name = 'authors').exists()
       return context
  
# Добавляем функциональное представление для повышения привилегий пользователя до членства в группе premium
@login_required
def upgrade_me(request):
   user = request.user
   author_group = Group.objects.get(name='authors')
   if not request.user.groups.filter(name='authors').exists():
       author_group.user_set.add(user)
   return redirect('/')


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'sign/signup.html'
    success_url = '/'
   
    def form_valid(self, form):
        user = form.save()
        logger.info("Creating a new group or getting existing one")
        group, created = Group.objects.get_or_create(name='common')
        if created:
            logger.info("New group created")
        else:
            logger.info("Group already exists")
        user.groups.add(group)
        return super().form_valid(form)

class LoginView(FormView):
   model = User
   form_class = LoginForm
   template_name = 'sign/login.html'
   success_url = '/'
  
   def form_valid(self, form):
       username = form.cleaned_data.get('username')
       password = form.cleaned_data.get('password')
       user = authenticate(self.request,username=username, password=password)
       if user is not None:
           login(self.request, user)
       return super().form_valid(form)
  
  
class LogoutView(LoginRequiredMixin, TemplateView):
   template_name = 'sign/logout.html'
  
   def get(self, request, *args, **kwargs):
       logout(request)
       return super().get(request, *args, **kwargs)