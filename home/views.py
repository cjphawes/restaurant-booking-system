from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/index.html'


class AboutView(TemplateView):
    template_name = 'home/about.html'


class FaqView(TemplateView):
    template_name = 'home/faq.html'
