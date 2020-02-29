from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('<int:listing_id>/', views.detail, name='detaillisting')
]