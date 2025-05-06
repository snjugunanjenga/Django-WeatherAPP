# WeatherApp

WeatherApp is a Django-based web application that provides real-time weather information. It allows users to search for weather data in various locations, save favorite locations, and set a default location for quick access. The app integrates with the OpenWeatherMap API to fetch weather data.

## Live Demo
- [WeatherApp Live Demo](https://django-weather-app-kenya.vercel.app/)
- [GitHub Repository](https://github.com/snjugunanjenga/Django-WeatherAPP.git)

## Features

- **Real-Time Weather Information**: Displays current weather details such as temperature, condition, humidity, and wind speed.
- **User Authentication**: Users can register, log in, and log out securely.
- **Search Functionality**: Search for weather information by entering a location.
- **Favorites Management**: Authenticated users can save and view their favorite locations.
- **Default Location**: Users can set a default location for quick weather updates.
- **Responsive Design**: Built with Bootstrap for a mobile-friendly interface.
- **Weather Icons**: Dynamic weather icons that change based on current conditions.
- **Temperature Units**: Support for both Celsius and Fahrenheit.
- **Error Handling**: Graceful error handling for API failures and invalid locations.
- **User Dashboard**: Personalized dashboard showing saved locations and weather updates.
- **Mobile-First Design**: Fully responsive layout that works on all devices.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.10 or higher
- Django 5.0.2
- A valid API key from [OpenWeatherMap](https://openweathermap.org/api)

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/snjugunanjenga/Django-WeatherAPP.git
   cd WeatherApp
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the project root
   - Add your OpenWeatherMap API key:
   ```
   WEATHER_API_KEY=your_api_key_here
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ```

5. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Open your browser and navigate to `http://127.0.0.1:8000/`
2. Register for an account or log in if you already have one
3. Search for weather information by entering a location in the search bar
4. Save favorite locations or set a default location for quick access
5. View detailed weather information including temperature, humidity, and wind speed
6. Toggle between Celsius and Fahrenheit temperature units

## Project Structure

```
WeatherApp/
├── WeatherApp/                # Main project folder
│   ├── settings.py            # Django settings
│   ├── urls.py                # Project-level URL configuration
│   ├── wsgi.py                # WSGI entry point
│   └── asgi.py                # ASGI entry point
├── weather/                   # Weather app folder
│   ├── templates/weather/     # HTML templates
│   ├── static/                # Static files (CSS, JS, images)
│   ├── models.py              # Database models
│   ├── views.py               # Application logic
│   ├── urls.py                # App-level URL configuration
│   ├── admin.py               # Admin panel configuration
│   ├── tests.py               # Unit tests
│   └── migrations/            # Database migrations
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
└── .env                       # Environment variables
```

## Deployment

The application is deployed on Vercel. To deploy your own version:

1. Fork the repository
2. Create a Vercel account
3. Connect your GitHub repository to Vercel
4. Set up the required environment variables in Vercel
5. Deploy!

## Future Enhancements

- Add support for hourly and weekly weather forecasts
- Implement a dashboard for user-specific analytics
- Add email notifications for weather alerts
- Include air quality index information
- Add weather maps and radar
- Implement location-based weather alerts
- Add historical weather data visualization

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Commit your changes and push them to your fork
4. Submit a pull request

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

**Simon Njuguna**
- Email: simonnjenganjuguna@gmail.com
- GitHub: [@snjugunanjenga](https://github.com/snjugunanjenga)

## Acknowledgments

- Django Documentation
- OpenWeatherMap API
- Bootstrap
- Vercel for hosting