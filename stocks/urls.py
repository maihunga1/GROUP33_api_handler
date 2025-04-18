# stocks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('daily/<str:ticker>/', views.daily, name='daily'),
    path('daily', views.daily_all, name='daily_all'),
    path('minutely', views.minutely_all, name='minutely_all'),
    path('minutely/<str:ticker>/', views.minutely, name='minute'),
    path('hourly', views.hourly_all, name='hourly_all'),
    path('hourly/<str:ticker>/', views.hourly, name='hourly'),
    path('monthly', views.monthly_all, name='monthly_all'),
    path('monthly/<str:ticker>/', views.monthly, name='monthly'),
    path('yearly', views.yearly_all, name='yearly_all'),
    path('yearly/<str:ticker>/', views.yearly, name='yearly'),
]