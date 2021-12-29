from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST.get("city")

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=<your_api_key>').read()

        list_of_data = json.loads(source)
        data = {
            "country_code": str(list_of_data["sys"]["country"]),
            "coordinate": str(list_of_data["coord"]["lon"]) + ' ' + str(list_of_data["coord"]["lat"]),
            "temp": str(list_of_data["main"]["temp"]) + ' C',
            "pressure": str(list_of_data["main"]["pressure"]),
            "humidity": str(list_of_data["main"]["humidity"])
        }
    else:
        data = {}
        return render(request,"index.html",{"data": data})

    return render(request,"index.html",{"data": data})
