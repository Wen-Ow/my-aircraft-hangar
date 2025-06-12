import django.forms as forms
from .models import Aircraft

class AddAircraftForm(forms.ModelForm):
    class Meta:
        model = Aircraft
        fields = ['tail_number', 'aircraft_type', 'model', 'category', 'manufacturer', 'condition', 'year', 'image', 'notes']
        widgets = {
            'tail_number': forms.TextInput(attrs={'placeholder': 'Tail Number'}),
            'aircraft_type': forms.Select(attrs={'placeholder': 'Aircraft Type'}),
            'model': forms.TextInput(attrs={'placeholder': 'Model'}),
            'category': forms.Select(attrs={'placeholder': 'Category'}),
            'manufacturer': forms.TextInput(attrs={'placeholder': 'Manufacturer'}),
            'condition': forms.TextInput(attrs={'placeholder': 'Condition'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Year'}),
            'image': forms.ClearableFileInput(),
            'notes': forms.Textarea(attrs={'placeholder': 'Notes', 'rows': 4}),
        }