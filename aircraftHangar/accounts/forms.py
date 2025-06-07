import django.forms as forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your account form
class RegisterUserForm(UserCreationForm):
    email: forms.EmailField(required=True, help_text='Required. Inform a valid email address.')
    first_name: forms.CharField(max_length=30, required=True, help_text='Required. Inform a valid first name.')
    last_name: forms.CharField(max_length=30, required=True, help_text='Required. Inform a valid last name.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }
    
# Login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True)

    error_messages = {
        'invalid_login': {
            'message': "Please enter a correct username and password.",
        },
    }
