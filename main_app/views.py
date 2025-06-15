from django.shortcuts import render
from aircraft.models import Aircraft
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    aircrafts = Aircraft.objects.all()
    context = {
        'aircrafts': aircrafts,
        'user': request.user
    }
    print(request.user.first_name)
    return render(request, 'main_app/home.html', context)