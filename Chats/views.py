from django.shortcuts import render,redirect
from django.views.generic import CreateView, ListView, TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import RedirectView
from .forms import SignUpForm
from django.contrib.auth import login
from django.urls import reverse_lazy
# Create your views here.

class IndexRedirectView(LoginRequiredMixin, RedirectView):
    pattern_name = 'frontpage'

class ShowView(TemplateView):
    template_name='./Chats/frontpage.html'

class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'Chats/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    

class LoginView():
    template_name = 'Chats/login.html'
    success_url = reverse_lazy('frontpage')


class LogoutView():
    next_page = reverse_lazy('frontpage') 

# def Signup(request):
#     if request.method == 'POST':
#         form=SignUpForm(request.POST)

#         if form.is_valid():
#             user=form.save()

#             login(request, user)
#             return redirect('front-page')
#         else:
#             form=SignUpForm()
#         return render(request, 'Chats/signup.html', {'form': form})
