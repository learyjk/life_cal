from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:week_number>/', views.week_view, name='week_view'),
]
