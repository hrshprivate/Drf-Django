from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView, DetailView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeForm

from .views import RegisterFormView, LoginFormView

urlpatterns = [
    path('', views.main_page, name='home'),
    path('not_home1337', views.notmainpage, name='not_home'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('signup/', views.RegisterFormView.as_view(), name='signup'),
    path('error/', views.error, name='error'),
    path('mail/', views.mail, name='mail'),
    path('logout/', views.user_delete, name='logout'),
    path('changePassword/', views.PasswordsChangeView.as_view(template_name='main/pass_change.html'), name='changePassword')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
