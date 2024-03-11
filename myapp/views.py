from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

#class from which all class based views inherit
class BaseView(TemplateView):
    default_title = 'My Website'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault('title', self.default_title)
        return context

class ClassView(BaseView):
  template_name = 'bootswatch.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': 'Class-Based View',
          'page_heading': 'Welcome to the Class-Based View',
          'page_content': 'This is the content generated by the class-based view.',
      })
      return context

class HomeView(BaseView):
  template_name = 'bootswatch.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': 'Home',
          'page_heading': 'Home Page',
          'page_content': 'Info on the home page.',
      })
      return context

class AboutView(BaseView):
  template_name = 'bootswatch.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': 'About',
          'page_heading': 'About',
          'page_content': 'Info on the About page.',
      })
      return context

class ThemeView(BaseView):
  template_name = 'theme.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # Add additional context data if needed
      return context

  def post(self, request, *args, **kwargs):
      theme = request.POST.get('theme')
      response = HttpResponseRedirect(reverse('theme'))
      response.set_cookie('theme', theme)
      return response

from django.http import JsonResponse
from .default_data import load_default_data

def load_default_data_view(request):
    load_default_data()  # Call the load_default_data function
    return JsonResponse({'status': 'success'})

from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Invention

class InventionListView(ListView):
    model = Invention
    template_name = 'invention_list.html'
    context_object_name = 'inventions'

from django.views.generic import DetailView
from .models import Invention

class InventionDetailView(DetailView):
    model = Invention
    template_name = 'invention_view.html'
    context_object_name = 'invention'
