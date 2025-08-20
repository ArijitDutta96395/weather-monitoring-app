# Weather Monitoring App

A modern, responsive Django web application that provides real-time weather information for cities worldwide. Built with Django framework and integrated with OpenWeatherMap API and Google Custom Search API for dynamic city imagery.

## 🌟 Features

- **Real-time Weather Data**: Get current weather conditions for any city
- **Dynamic City Images**: Beautiful background images that change based on the searched city
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Error Handling**: Graceful handling of API errors and unavailable data
- **User-Friendly Interface**: Clean, modern UI with intuitive search functionality
- **Temperature Display**: Shows temperature in Celsius with weather icons
- **Weather Descriptions**: Detailed weather conditions and descriptions

## 🛠️ Tech Stack

- **Backend**: Django 4.x
- **Frontend**: HTML5, CSS3, JavaScript
- **APIs**: 
  - OpenWeatherMap API for weather data
  - Google Custom Search API for city images
- **Styling**: Custom CSS with responsive design
- **Fonts**: Google Fonts (Poppins)

## 📋 Prerequisites

Before running this project, make sure you have the following installed:
- Python 3.8 or higher
- Django 4.x
- pip (Python package manager)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/weather-monitoring-app.git
cd weather-monitoring-app
```

### 2. Navigate to Project Directory
```bash
cd weatherproject
```

### 3. Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure API Keys

Create a `.env` file in the project root and add your API keys:

```env
OPENWEATHER_API_KEY=your_openweather_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id_here
```

### 6. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Start the Development Server
```bash
python manage.py runserver
```

### 8. Access the Application
Open your browser and navigate to: `http://localhost:8000`

## 🔧 API Configuration

### OpenWeatherMap API
1. Sign up at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your free API key from the dashboard
3. Add the key to your `.env` file

### Google Custom Search API
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable Custom Search API
4. Create credentials (API Key)
5. Set up a Custom Search Engine at [Google Custom Search](https://cse.google.com/cse/)
6. Add both API key and Search Engine ID to your `.env` file

## 📁 Project Structure

```
weather-monitoring-app/
├── weatherproject/
│   ├── weatherapp/
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── weatherapp/
│   │   │       └── index.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── weatherproject/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── static/
│   │   └── style.css
│   ├── db.sqlite3
│   └── manage.py
├── README.md
└── requirements.txt
```

## 🎯 Usage

1. **Search for Weather**: Enter any city name in the search bar and click "Search"
2. **View Results**: See current temperature, weather description, and city-specific background
3. **Responsive Design**: The app adapts to your screen size automatically
4. **Error Handling**: If a city is not found, you'll see an appropriate error message

## 🎨 Customization

### Styling
- Modify `static/style.css` to change colors, fonts, or layout
- Update CSS variables in `:root` for theme customization

### Templates
- Edit `weatherapp/templates/weatherapp/index.html` to change the HTML structure
- Add new templates in the `templates` directory for additional pages

### API Endpoints
- Modify the weather API URL in `views.py` to use different weather services
- Add new API integrations in the `views.py` file

## 🔍 API Endpoints

- **GET /** - Main weather display page
- **POST /** - Handle city search form submission

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Ensure your API keys are correctly added to the `.env` file
   - Check if the APIs are enabled in your respective accounts

2. **Import Errors**
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Verify your virtual environment is activated

3. **Static Files Not Loading**
   - Run `python manage.py collectstatic` in production
   - Check `STATIC_URL` and `STATICFILES_DIRS` in settings.py

4. **Database Issues**
   - Run migrations: `python manage.py makemigrations && python manage.py migrate`
   - Check database configuration in settings.py

## 🚀 Deployment

### Using Heroku
```bash
# Install Heroku CLI
# Create Heroku app
heroku create your-weather-app

# Add buildpacks
heroku buildpacks:add heroku/python
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-static

# Set environment variables
heroku config:set OPENWEATHER_API_KEY=your_key
heroku config:set GOOGLE_API_KEY=your_key
heroku config:set GOOGLE_SEARCH_ENGINE_ID=your_id

# Deploy
git push heroku main
```

### Using PythonAnywhere
1. Create account at [PythonAnywhere](https://www.pythonanywhere.com/)
2. Upload your project files
3. Configure virtual environment and settings
4. Set up static files mapping

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing weather data
- [Google Custom Search API](https://developers.google.com/custom-search) for city images
- [Django](https://www.djangoproject.com/) for the web framework
- [Poppins Font](https://fonts.google.com/specimen/Poppins) for typography

## 📞 Contact

For questions or support, please open an issue on GitHub or contact the maintainers.

---

**Happy Weather Watching!** 🌤️
