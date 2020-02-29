from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'), 
    path('<int:agent_id>/', views.detail, name='detail'),
]