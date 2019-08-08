from django.http import HttpResponse
from django.shortcuts import render

from cadastro.models import Person


def hello(request):
    return render(request, 'index.html')

def person(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'pessoas': persons})