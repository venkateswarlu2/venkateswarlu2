from django import forms
from .models import SignUp

# myapp/forms.py
from django import forms
from .models import SignUp
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email', 'phone_number', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
class EmailAuthenticatForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'autofocus':True}))


