from django.urls import path
from . import views

urlpatterns = [
  path("",views.HomeView.as_view(), name="home"),
  path("about/",views.AboutView.as_view(), name="about"),
  path('class/', views.ClassView.as_view(), name='class_view'),
  path('theme/', views.ThemeView.as_view(), name='theme'),
  path('load/', views.load_default_data_view, name='load_default_data'),
  path('inventions/', views.InventionListView.as_view(), name='invention-list'),
  path('invention/<int:pk>/', views.InventionDetailView.as_view(), name='invention-view'),
]





