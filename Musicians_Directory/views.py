from django.shortcuts import render
from musician.models import Musician
# Create your views here.
def home(request):
    data = Musician.objects.all()
    print(data)
    return render(request, 'index.html', {'data': data})