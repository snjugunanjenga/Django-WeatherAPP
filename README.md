# WeatherApp

WeatherApp is a Django-based web application that provides real-time weather information. It allows users to search for weather data in various locations, save favorite locations, and set a default location for quick access. The app integrates with the OpenWeatherMap API to fetch weather data.

---

## Features

- **Real-Time Weather Information**: Displays current weather details such as temperature, condition, humidity, and wind speed.
- **User Authentication**: Users can register, log in, and log out securely.
- **Search Functionality**: Search for weather information by entering a location.
- **Favorites Management**: Authenticated users can save and view their favorite locations.
- **Default Location**: Users can set a default location for quick weather updates.
- **Responsive Design**: Built with Bootstrap for a mobile-friendly interface.

---

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.10 or higher
- Django 5.1.7
- A valid API key from [OpenWeatherMap](https://openweathermap.org/api)

---

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd WeatherApp
   ```

2. Create and Activate a Virtual Environment:
```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependencies:
```
    pip install -r requirements.txt
```
4. Set Up Environment Variables:

    - Create a .env file in the project root.
    - Add your OpenWeatherMap API key:
```
    WEATHER_API_KEY=your_api_key_here
```
5. Apply Migrations:
```
    python makemigrations
    python migrate
```
6. Run the Development Server:
``` 
    python  runserver
```
## Usage
1. Open your browser and navigate to http://127.0.0.1:8000/.
2. Register for an account or log in if you already have one.
3. Search for weather information by entering a location in the search bar.
4. Save favorite locations or set a default location for quick access.

## Project Structure
```
WeatherApp/
├── WeatherApp/                # Main project folder
│   ├──  settings.py           # Django settings
│   ├──  urls.py               # Project-level URL configuration
│   ├──   wsgi.py              # WSGI entry point
│   └──   asgi.py              # ASGI entry point
├── weather/                   # Weather app folder
│   ├── templates/weather/     # HTML templates
│   ├── static/                # Static files (CSS, JS, images)
│   ├── model              # Database models
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
## Key Features in Detail
1. **Weather Search**
    - Users can search for weather information by entering a       location.
    - The app fetches data from the OpenWeatherMap API and displays:
        - Temperature
        - Weather condition
        - Humidity
        - Wind speed
        - Weather icon
2. **User Authentication**
    - Users can register, log in, and log out.
    - Authentication is required to save favorite locations or set a default location.
3. **Favorites Management**
Authenticated users can save locations as favorites.
View all saved favorite locations on a dedicated page.
4. **Default Location**
Users can set a default location, which will be displayed automatically on the homepage.

## API Integration
The app uses the OpenWeatherMap API to fetch weather data. Ensure you have a valid API key and add it to the .env file as shown in the installation steps.

## Screenshots
Homepage


## Future Enhancements
    - Add support for hourly and weekly weather forecasts.
    - Implement a dashboard for user-specific analytics.
    - Add email notifications for weather alerts.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
    - Collecting workspace informationHere is a detailed README.md for your Weather App:

```markdown
# WeatherApp

WeatherApp is a Django-based web application that provides real-time weather information. It allows users to search for weather data in various locations, save favorite locations, and set a default location for quick access. The app integrates with the OpenWeatherMap API to fetch weather data.

---

## Features

- **Real-Time Weather Information**: Displays current weather details such as temperature, condition, humidity, and wind speed.
- **User Authentication**: Users can register, log in, and log out securely.
- **Search Functionality**: Search for weather information by entering a location.
- **Favorites Management**: Authenticated users can save and view their favorite locations.
- **Default Location**: Users can set a default location for quick weather updates.
- **Responsive Design**: Built with Bootstrap for a mobile-friendly interface.

---

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.10 or higher
- Django 5.1.7
- A valid API key from [OpenWeatherMap](https://openweathermap.org/api)

---

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
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
   - Create a `.env` file in the project root.
   - Add your OpenWeatherMap API key:
     ```
     WEATHER_API_KEY=your_api_key_here
     ```

5. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

---

## Usage

1. Open your browser and navigate to `http://127.0.0.1:8000/`.
2. Register for an account or log in if you already have one.
3. Search for weather information by entering a location in the search bar.
4. Save favorite locations or set a default location for quick access.

---

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

---

## Key Features in Detail

### 1. Weather Search
- Users can search for weather information by entering a location.
- The app fetches data from the OpenWeatherMap API and displays:
  - Temperature
  - Weather condition
  - Humidity
  - Wind speed
  - Weather icon

### 2. User Authentication
- Users can register, log in, and log out.
- Authentication is required to save favorite locations or set a default location.

### 3. Favorites Management
- Authenticated users can save locations as favorites.
- View all saved favorite locations on a dedicated page.

### 4. Default Location
- Users can set a default location, which will be displayed automatically on the homepage.

---

## API Integration

The app uses the OpenWeatherMap API to fetch weather data. Ensure you have a valid API key and add it to the `.env` file as shown in the installation steps.

---

## Screenshots

### Homepage
![Homepage](https://via.placeholder.com/800x400?text=Homepage)

### Weather Search
![Weather Search](https://via.placeholder.com/800x400?text=Weather+Search)

### Favorites
![Favorites](https://via.placeholder.com/800x400?text=Favorites)

---

## Future Enhancements

- Add support for hourly and weekly weather forecasts.
- Implement a dashboard for user-specific analytics.
- Add email notifications for weather alerts.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Bootstrap](https://getbootstrap.com/)
```

This README provides a comprehensive overview of the project, including setup instructions, features, and future enhancements.