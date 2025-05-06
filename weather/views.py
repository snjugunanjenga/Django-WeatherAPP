from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests
import os
from dotenv import load_dotenv
from .models import FavoriteLocation, FarmerProfile, PilotProfile
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from datetime import datetime, timedelta
import json





load_dotenv()  # Load environment variables from .env

def demo_login(request):
    # Create a demo user if it doesn't exist
    demo_user, created = User.objects.get_or_create(
        username='demo_user',
        defaults={'email': 'demo@example.com', 'is_active': True}
    )
    if created:
        demo_user.set_password('demo_password')
        demo_user.save()
    # Log in the demo user
    login(request, demo_user)
    return redirect('index')


@login_required
def index(request):
    location = request.GET.get('location')
    weather_data = None
    forecast = None
    alerts = None
    weather_stations = None
    planting_recommendations = None
    wind_shear_risk = None
    metar_taf_data = None
    soil_moisture_dates = None
    soil_moisture_values = None
    
    if location:
        # Get current weather data
        weather_data = get_weather_data(location)
        if weather_data:
            # Get forecast data
            forecast = get_forecast_data(location)
            # Get weather alerts
            alerts = get_weather_alerts(location)
            # Get nearby weather stations
            weather_stations = get_weather_stations(weather_data['lat'], weather_data['lon'])
            
            # Get specialized information based on user profile
            if request.user.is_authenticated:
                if hasattr(request.user, 'farmerprofile'):
                    planting_recommendations = get_planting_recommendations(weather_data)
                    soil_moisture_data = get_soil_moisture_forecast(location)
                    soil_moisture_dates = json.dumps(soil_moisture_data['dates'])
                    soil_moisture_values = json.dumps(soil_moisture_data['values'])
                
                if hasattr(request.user, 'pilotprofile'):
                    wind_shear_risk = calculate_wind_shear_risk(weather_data)
                    metar_taf_data = get_metar_taf_data(location)
    
    context = {
        'weather_data': weather_data,
        'forecast': forecast,
        'alerts': alerts,
        'weather_stations': weather_stations,
        'planting_recommendations': planting_recommendations,
        'wind_shear_risk': wind_shear_risk,
        'metar_taf_data': metar_taf_data,
        'soil_moisture_dates': soil_moisture_dates,
        'soil_moisture_values': soil_moisture_values,
    }
    return render(request, 'weather/index.html', context)

def get_weather_data(location):
    # OpenWeatherMap API call
    api_key = os.getenv('WEATHER_API_KEY')  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            return {
                'location': location,
                'temperature': round(data['main']['temp']),
                'condition': data['weather'][0]['main'],
                'icon': data['weather'][0]['icon'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'visibility': round(data['visibility'] / 1000),  # Convert to km
                'lat': data['coord']['lat'],
                'lon': data['coord']['lon']
            }
    except Exception as e:
        print(f"Error fetching weather data: {e}")
    
    return None

def get_forecast_data(location):
    api_key = os.getenv('WEATHER_API_KEY')  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            forecast = []
            current_date = None
            
            for item in data['list']:
                date = datetime.fromtimestamp(item['dt']).date()
                
                if date != current_date:
                    if current_date is not None:
                        forecast.append(day_data)
                    
                    current_date = date
                    day_data = {
                        'date': date,
                        'temp_max': round(item['main']['temp_max']),
                        'temp_min': round(item['main']['temp_min']),
                        'icon': item['weather'][0]['icon']
                    }
                else:
                    day_data['temp_max'] = max(day_data['temp_max'], round(item['main']['temp_max']))
                    day_data['temp_min'] = min(day_data['temp_min'], round(item['main']['temp_min']))
            
            if current_date is not None:
                forecast.append(day_data)
            
            return forecast[:7]  # Return 7-day forecast
    except Exception as e:
        print(f"Error fetching forecast data: {e}")
    
    return None

def get_weather_alerts(location):
    # This is a placeholder. In a real application, you would integrate with a weather alert API
    return [
        {
            'title': 'Heavy Rainfall Warning',
            'description': 'Heavy rainfall expected in the next 24 hours.',
            'severity': 'warning'
        }
    ]

def get_weather_stations(lat, lon):
    # This is a placeholder. In a real application, you would integrate with a weather station API
    return [
        {
            'name': 'Nairobi Weather Station',
            'lat': -1.2921,
            'lon': 36.8219
        },
        {
            'name': 'Mombasa Weather Station',
            'lat': -4.0435,
            'lon': 39.6682
        }
    ]

def get_planting_recommendations(weather_data):
    # This is a placeholder. In a real application, you would implement actual planting recommendations
    return "Based on current weather conditions, it's a good time to plant maize and beans."

def get_soil_moisture_forecast(location):
    # This is a placeholder. In a real application, you would integrate with a soil moisture API
    dates = [(datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]
    values = [65, 68, 70, 72, 75, 73, 70]  # Example soil moisture values
    return {'dates': dates, 'values': values}

def calculate_wind_shear_risk(weather_data):
    # This is a placeholder. In a real application, you would implement actual wind shear calculations
    return 25  # Example risk percentage

def get_metar_taf_data(location):
    # This is a placeholder. In a real application, you would integrate with an aviation weather API
    return "METAR: HKNX 121200Z 08008KT 9999 FEW020 SCT040 24/18 Q1013 NOSIG\nTAF: HKNX 121200Z 1212/1312 08008KT 9999 FEW020 SCT040"

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create appropriate profile based on email domain
            if user.email.endswith('@farmer.com'):
                FarmerProfile.objects.create(user=user)
            elif user.email.endswith('@pilot.com'):
                PilotProfile.objects.create(user=user)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'weather/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'weather/login.html', {'form': form, 'next': request.GET.get('next')})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def favorites(request):
    favorites = FavoriteLocation.objects.filter(user=request.user)
    weather_data_list = []
    
    for favorite in favorites:
        weather_data = get_weather_data(favorite.location)
        if weather_data:
            weather_data['id'] = favorite.id  # Add the favorite location ID
            weather_data_list.append(weather_data)
        else:
            weather_data_list.append({
                'id': favorite.id,  # Add the favorite location ID
                'location': favorite.location,
                'error': 'Unable to fetch weather data'
            })
    
    return render(request, 'weather/favorites.html', {'weather_data_list': weather_data_list})

@login_required
def add_favorite(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        if location:
            FavoriteLocation.objects.get_or_create(user=request.user, location=location)
            messages.success(request, f'{location} added to favorites.')
    return redirect('index')

@login_required
def remove_favorite(request, location_id):
    favorite = FavoriteLocation.objects.get(id=location_id, user=request.user)
    favorite.delete()
    return redirect('favorites')

@login_required
def set_default_location(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        if location:
            if hasattr(request.user, 'farmerprofile'):
                request.user.farmerprofile.default_location = location
                request.user.farmerprofile.save()
            elif hasattr(request.user, 'pilotprofile'):
                request.user.pilotprofile.default_location = location
                request.user.pilotprofile.save()
            messages.success(request, f'Default location set to {location}.')
    return redirect('index')

@login_required
def farmer_dashboard(request):
    if not hasattr(request.user, 'farmerprofile'):
        messages.error(request, 'You must be a farmer to access this page.')
        return redirect('index')
    
    # Get farmer-specific data
    context = {
        'planting_calendar': get_planting_calendar(),
        'crop_recommendations': get_crop_recommendations(),
        'market_prices': get_market_prices()
    }
    return render(request, 'weather/farmer_dashboard.html', context)

@login_required
def pilot_dashboard(request):
    if not hasattr(request.user, 'pilotprofile'):
        messages.error(request, 'You must be a pilot to access this page.')
        return redirect('index')
    
    # Get pilot-specific data
    context = {
        'flight_conditions': get_flight_conditions(),
        'airport_status': get_airport_status(),
        'flight_routes': get_flight_routes()
    }
    return render(request, 'weather/pilot_dashboard.html', context)

# Placeholder functions for dashboard data
def get_planting_calendar():
    return [
        {'crop': 'Maize', 'planting_date': '2024-03-15', 'harvest_date': '2024-07-15'},
        {'crop': 'Beans', 'planting_date': '2024-03-20', 'harvest_date': '2024-06-20'}
    ]

def get_crop_recommendations():
    return [
        {'crop': 'Maize', 'variety': 'H614', 'suitable_regions': ['Central', 'Rift Valley']},
        {'crop': 'Beans', 'variety': 'GLP-2', 'suitable_regions': ['Western', 'Nyanza']}
    ]

def get_market_prices():
    return [
        {'crop': 'Maize', 'price': 2500, 'unit': '90kg bag'},
        {'crop': 'Beans', 'price': 3500, 'unit': '90kg bag'}
    ]

def get_flight_conditions():
    return [
        {'airport': 'JKIA', 'visibility': '10km', 'wind': '8kt', 'ceiling': '3000ft'},
        {'airport': 'Moi International', 'visibility': '8km', 'wind': '12kt', 'ceiling': '2500ft'}
    ]

def get_airport_status():
    return [
        {'airport': 'JKIA', 'status': 'Open', 'runway_condition': 'Dry'},
        {'airport': 'Moi International', 'status': 'Open', 'runway_condition': 'Wet'}
    ]

def get_flight_routes():
    return [
        {'route': 'Nairobi-Mombasa', 'distance': '440km', 'estimated_time': '45min'},
        {'route': 'Nairobi-Kisumu', 'distance': '265km', 'estimated_time': '35min'}
    ]