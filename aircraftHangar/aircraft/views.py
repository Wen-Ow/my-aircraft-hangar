from django.shortcuts import render, redirect
from .models import AircraftType, Category
from .forms import AddAircraftForm

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