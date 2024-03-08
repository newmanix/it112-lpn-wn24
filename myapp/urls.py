from django.urls import path
from . import views

urlpatterns = [
  path("",views.HomeView.as_view(), name="home"),
  path("about/",views.AboutView.as_view(), name="about"),
  path('class/', views.ClassView.as_view(), name='class_view'),
  path('theme/', views.ThemeView.as_view(), name='theme'),
]

