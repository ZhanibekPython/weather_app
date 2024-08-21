import requests
from django.conf import settings
from django.shortcuts import render
from fake_useragent import UserAgent
from datetime import date

fake_agent = UserAgent()


# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}


def weather(request):
    headers = {
        'User-Agent': fake_agent.random
    }
    if request.method == 'GET':
        return render(request, 'weather/index.html')

    if request.method == 'POST':
        city = request.POST.get('city').capitalize().strip()

        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.MY_API_KEY}&units=metric",
                                headers=headers).json()

        cloudiness = response['weather'][0]['description'].capitalize()
        temp = response['main']['temp']
        feels_like = response['main']['feels_like']
        pressure = response['main']['pressure']
        humidity = response['main']['humidity']

        return render(request, 'weather/index.html', context={
            'result': response,
            'city': city.capitalize(),
            'cloudiness': cloudiness,
            'temp': temp,
            'feels_like': feels_like,
            'pressure': pressure,
            'humidity': humidity,
        })