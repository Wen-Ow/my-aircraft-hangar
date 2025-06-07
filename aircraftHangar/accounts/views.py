from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Register View
def registerView(request):
    # If the user is already authenticated, redirect to home
    if request.user.is_authenticated:
        return render(request, 'main_app/home.html')

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
           print("Form is valid")
           form.save()
           return redirect('login')  # Redirect to login page after successful registration
        else:
            print(form.errors)
    else:
        form = RegisterUserForm()
        context = {
            'form': form,
        }
    return render(request, 'accounts/register.html', context)

# Login View
def loginView(request):
    # If the user is already authenticated, redirect to home
    if request.user.is_authenticated:
        return render(request, 'main_app/home.html')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate User
        user = authenticate(request, username=username, password=password)
        #if User exists
        if user is not None:
            # Login the user
            login(request, user)
            print("User authenticated successfully")
            return redirect('home')  # Redirect to home page after successful login
        else:
            print("Invalid username or password")
            return redirect('login')
    else:
        form = LoginForm()
        context = {
            'form': form,
        }
    return render(request, 'accounts/login.html', context)


# Logout View
def logoutView(request):
    logout(request)
    print("User logged out successfully")
    return redirect('login')  # Redirect to login page after logout