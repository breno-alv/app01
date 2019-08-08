from django.shortcuts import render
from .models import Person

# Create your views here.

def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'person': persons})