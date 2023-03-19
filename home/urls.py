from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('FAQ/', views.faq, name='FAQ'),
    path('become-an-agent/', views.become, name='become'),
]
