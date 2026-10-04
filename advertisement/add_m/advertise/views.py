from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Homepage view
def home(request):
    return render(request, 'home.html')

# Registration view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Dashboard view (only for logged-in users)
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from .models import UserProfile

@login_required
def edit_profile(request):
    profile = request.user.userprofile

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})
from django.shortcuts import render, redirect
from .models import Campaign
from django.contrib.auth.decorators import login_required

@login_required
def campaign_list(request):
    campaigns = Campaign.objects.filter(user=request.user)
    return render(request, 'campaigns.html', {'campaigns': campaigns})

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, "Your profile has been deleted.")
        return redirect('home')  # Redirect to your homepage or login
    return render(request, 'delete_profile.html')

