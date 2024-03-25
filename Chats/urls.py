from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import ShowView, SignUpView
# LoginView, IndexRedirectView

urlpatterns = [
    # path('', IndexRedirectView.as_view(), name='index'),
    path('', SignUpView.as_view(), name='signup'),
    path('frontpage/', ShowView.as_view(), name='frontpage'),
    path('login/', auth_views.LoginView.as_view(template_name='Chats/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('login/', LoginView.as_view(), name='login'),
    
]
