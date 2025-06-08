from django.urls import path, include
from . import views


urlpatterns = [
    # Create Aircraft Route
    path('create/', views.addView, name='create_aircraft')
]