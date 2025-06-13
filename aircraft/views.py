from django.shortcuts import render, redirect
from .models import Aircraft, AircraftType, Category
from .forms import AddAircraftForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def addView(request):
    if request.method == 'POST':
        # Handle form submission
        form = AddAircraftForm(request.POST, request.FILES)
        if form.is_valid():
            aircraft_entry = form.save(commit=False)
            # Set the user to the currently logged-in user
            aircraft_entry.user = request.user
            # Save the aircraft entry to the database
            aircraft_entry.save()
            # Redirect to the aircraft list or detail page after successful submission
            return redirect('home')          
    else:
        # Fetch all aircraft types to display in the form
        aircraft_types = AircraftType.objects.all()
        # Fetch all categories to display in the form
        categories = Category.objects.all()
        context = {
            'aircraft_types': aircraft_types,
            'categories': categories,
        }
        return render(request, 'aircraft/add.html', context)
    
@login_required(login_url='login')
def viewAircraft(request, pk):
    # Fetch the aircraft entry by primary key (pk)
    aircraft = Aircraft.objects.get(pk=pk)
    context = {
        'aircraft': aircraft
    }
    return render(request, 'aircraft/view.html', context)

@login_required(login_url='login')
def editAircraft(request, pk):
    # Fetch the aircraft entry by primary key (pk)
    aircraft = Aircraft.objects.get(pk=pk)
    
    if request.method == 'POST':
        # Handle form submission
        form = AddAircraftForm(request.POST, request.FILES, instance=aircraft)
        if form.is_valid():
            form.save()  # Save the updated aircraft entry to the database
            return redirect('home')  # Redirect to the home page after successful update
    else:
        # Pre-fill the form with existing data
        form = AddAircraftForm(instance=aircraft)
     # Fetch all aircraft types to display in the form
        aircraft_types = AircraftType.objects.all()
        # Fetch all categories to display in the form
        categories = Category.objects.all()
           
        context = {
            'form': form,
            'aircraft': aircraft,
            'aircraft_types': aircraft_types,
                'categories': categories,
        }
        return render(request, 'aircraft/edit.html', context)

@login_required(login_url='login')
def deleteAircraft(request, pk):
    # Fetch the aircraft entry by primary key (pk)
    aircraft = Aircraft.objects.get(pk=pk)
   
    aircraft.delete()
    return redirect('home')  # Redirect to the home page after deletion
   