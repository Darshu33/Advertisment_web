from django import forms
from django.contrib.auth.models import User
from .models import Customer

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone', 'address']

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio']
from django import forms
from .models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['title', 'description', 'image_url']
