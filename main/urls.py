from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign_up', views.register, name='sign_up'),
    path('login', views.login_form, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('exam', views.exam, name='exam'),
    path('user_answers/', views.display_user_answers),
    path('members/', views.members),


]
