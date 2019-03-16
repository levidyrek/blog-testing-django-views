from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.AddTwoNumbersView.as_view()),
]
