from django.urls import path

from . import views

app_name = 'addtwonumbers'
urlpatterns = [
    path('add/', views.AddTwoNumbersView.as_view(), name='add'),
]
