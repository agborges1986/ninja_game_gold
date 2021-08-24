from django.urls import path, include
from . import views
	
urlpatterns = [
	path('', views.index, name='index'),
    path('process_money/', views.process_money, name='process_money'),
    path('reset_game/', views.reset_game, name='reset'),
    path('config/', views.config_game, name='config'),
]
