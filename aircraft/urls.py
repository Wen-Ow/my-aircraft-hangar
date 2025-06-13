from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Create Aircraft Route
    path('create/', views.addView, name='create_aircraft'),
    path('view/<int:pk>/', views.viewAircraft, name='view_aircraft'),
    path('edit/<int:pk>/', views.editAircraft, name='edit_aircraft'),
    path('delete/<int:pk>/', views.deleteAircraft, name='delete_aircraft'),
]

# Add Static Files URL
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)