from django.shortcuts import render
import urllib.request
import json
import unicodedata
# Create your views here.

def index(request):
    if request.method == "POST":
        city = request.POST['city'].replace(' ','%20')
        city2 = unicodedata.normalize("NFD", city).encode("ascii", "ignore").decode("utf-8")
        source = urllib.request.urlopen(
            'sua-chave-da-api-openweathermap' + city2 + 
            '&units=metric&lang=PT-BR&appid=3ca183ea5f70bb99829c4d7bfa4e545a'
            ).read()
        list_of_data = json.loads(source)

        data = {
            'city': city.replace('%20',' ').upper(),
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']) + '%',
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']).upper(),
            'icon': list_of_data['weather'][0]['icon'],
        }
    else:
        data = {}

    return render(request, "main/index.html", data)
