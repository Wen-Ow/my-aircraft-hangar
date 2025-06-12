from django.shortcuts import render
from aircraft.models import Aircraft

# Create your views here.
def home(request):
    aircrafts = Aircraft.objects.all()
    context = {
        'aircrafts': aircrafts
    }
    return render(request, 'main_app/home.html', context)