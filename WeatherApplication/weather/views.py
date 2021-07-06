from django.shortcuts import redirect, render
import requests
from .models import City
from .forms import CityForm
from django.contrib import messages

def index(request):
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=YOUR_APP_KEY'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f233cf523e0bf623e825b40b696efce0'
    
    cities = City.objects.all() #return all the cities in the database

    if request.method == 'POST':    #only true if form is submitted
        form = CityForm(request.POST)   #add actual request data to form for processing
        if (requests.get(url.format(form.data["name"])).json()['cod'] == '404'):
            messages.info(request, "The city was not found in the API database!")
        elif len(cities.filter(name=(form.data["name"]).capitalize())) > 0:
            messages.info(request, "The city already exists in the database!")
        else:
            messages.info(request, "The city has been added to the database!")
            print(form)
            form.save() #will validate and save if validate

    
    form = CityForm

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        # print(city_weather) #temporarily view output

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)
    
    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/index.html', context) #returns the index.html template


def remove(request, item_id):
    item = City.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Item removed!")
    return redirect('weather')
    
