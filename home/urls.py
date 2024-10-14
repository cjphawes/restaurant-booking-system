from django.contrib import admin
from django.urls import path
from .views import HomeView, AboutView, FaqView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('faq/', FaqView.as_view(), name="faq")
]
