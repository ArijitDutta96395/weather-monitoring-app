from django.shortcuts import render, HttpResponse
from django.contrib import messages
import requests
import datetime

def home(request):
   
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = 'indore'     
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9a68329d67fce85279bc1f9d81889032'
    PARAMS = {'units':'metric'}

    # Google Custom Search API configuration
    API_KEY = 'AIzaSyCUTy4_GW-zr1ECA7dJwlPjpoFfSC2MCW8'  # Replace with actual API key
    SEARCH_ENGINE_ID = '127d93a3a85d4499e'  # Replace with actual search engine ID
    
    # Default fallback image URL
    default_image_url = 'https://images.pexels.com/photos/3008509/pexels-photo-3008509.jpeg?auto=compress&cs=tinysrgb&w=1600'
    image_url = default_image_url
    
    # Only attempt to fetch city-specific image if API keys are configured
    if API_KEY and SEARCH_ENGINE_ID and API_KEY.strip():
        try:
            query = city + " 1920x1080"
            page = 1
            start = (page - 1) * 10 + 1
            searchType = 'image'
            city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

            data = requests.get(city_url).json()
            search_items = data.get("items")
            
            if search_items and len(search_items) > 0:
                # Get the first image result
                image_url = search_items[0].get('link', default_image_url)
            else:
                image_url = default_image_url
                
        except Exception as e:
            # Fallback to default image if API call fails
            image_url = default_image_url
    else:
        # Use default image if API keys are not configured
        image_url = default_image_url

    try:
        data = requests.get(url,params=PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request,'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'exception_occurred': False,
            'image_url': image_url
        })
    
    except KeyError:
        exception_occurred = True
        messages.error(request,'Entered data is not available to API')   
        day = datetime.date.today()

        return render(request,'weatherapp/index.html', {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 35,
            'day': day,
            'city': 'kolkata',
            'exception_occurred': exception_occurred,
            'image_url': image_url
        })
