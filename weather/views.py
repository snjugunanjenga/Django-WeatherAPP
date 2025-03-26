
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests
import os
from dotenv import load_dotenv
from .models import UserProfile





load_dotenv()  # Load environment variables from .env

@login_required
def index(request):
    api_key = os.getenv('WEATHER_API_KEY')  # Ensure this is set in your .env file
    location = request.GET.get('location', 'Kenya')  # Default to Kenya if no location provided
    weather_data = None
    error_message = None

    if api_key:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'location': data['name'],
                'temperature': round(data['main']['temp'], 1),
                'condition': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            error_message = "Location not found or API error."
    else:
        error_message = "API key not found. Please set WEATHER_API_KEY in .env"

    context = {
        'weather_data': weather_data,
        'error_message': error_message,
    }
    return render(request, 'weather/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            default_location = request.POST.get('default_location')
            UserProfile.objects.create(user=user, default_location=default_location)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'weather/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'weather/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')

from .models import FavoriteLocation
@login_required
def favorites(request):
    api_key = os.getenv('WEATHER_API_KEY')
    favorites = FavoriteLocation.objects.filter(user=request.user)
    weather_data_list = []

    for favorite in favorites:
        location = favorite.location
        if api_key:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'location': data['name'],
                    'temperature': round(data['main']['temp'], 1),
                    'condition': data['weather'][0]['description'],
                    'humidity': data['main']['humidity'],
                    'wind_speed': data['wind']['speed'],
                    'icon': data['weather'][0]['icon'],
                }
                weather_data_list.append(weather_data)
            else:
                weather_data_list.append({'location': location, 'error': 'Location not found or API error.'})
        else:
            weather_data_list.append({'location': location, 'error': 'API key not found.'})

    context = {'weather_data_list': weather_data_list}
    return render(request, 'weather/favorites.html', context)

from django.shortcuts import redirect

@login_required
def add_favorite(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        if location:
            try:
                FavoriteLocation.objects.create(user=request.user, location=location)
                return redirect('favorites')
            except Exception as e:
                print(f"Error saving favorite: {e}")  # Check this in your server logs
                return render(request, 'weather/error.html', {'message': 'Failed to save favorite.'})
    return redirect('index')  # Redirect to homepage if not POST or location is missing

@login_required
def remove_favorite(request, location_id):
    favorite = FavoriteLocation.objects.get(id=location_id, user=request.user)
    favorite.delete()
    return redirect('favorites')

@login_required
def set_default_location(request):
    if request.method == 'POST':
        default_location = request.POST.get('default_location')
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        user_profile.default_location = default_location
        user_profile.save()
        return redirect('index')
    return render(request, 'weather/set_default_location.html')