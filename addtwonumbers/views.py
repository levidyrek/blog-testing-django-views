from django import forms
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.generic import View

from .app import math


class AddTwoNumbersForm(forms.Form):
    first = forms.DecimalField()
    second = forms.DecimalField()


class AddTwoNumbersView(View):
    def get(self, request):
        form = AddTwoNumbersForm(request.GET)
        if form.is_valid():
            params = form.cleaned_data
            result = math.add_two_numbers(params['first'], params['second'])
            return JsonResponse({'result': result})
        return HttpResponseBadRequest()
