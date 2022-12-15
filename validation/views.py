from django.shortcuts import render
from django.http import *
from .forms import *
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "validation/index.html"


def contact_form(request):
    form = ContactForm()
    return render(request, 'validation/contact.html', {'form': form})