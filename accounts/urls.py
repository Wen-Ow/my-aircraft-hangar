from django.urls import path, include
from . import views


urlpatterns = [
    # Register Route
    path('register/', views.registerView, name='register'),
    # Login Route
    path('login/', views.loginView, name='login'),
    # Logout Route
    path('logout/', views.logoutView, name='logout'),
]

# Add Static Files URL
urlpatterns += [
    path('static/', include('django.contrib.staticfiles.urls')),
]