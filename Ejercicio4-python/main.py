# Ejercicio 4
# Enunciado: Utilizando la API de https://openweathermap.org/ y realizando una petición
# a api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key},
# obtén la temperatura máxima y mínima, para la ciudad que proporcione el usuario.

# Objetivo:
# - Aprender a utilizar librerías externas (en este caso, requests)
# - Manipular el resultado de la petición (JSON)

#previsión a 7 días y haciendo la temperatura media
import requests
import statistics

def main():
    pass

city = ''

def tempMax(city):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=sp,es&appid=8803b5791abaa43c513206e31d9cdaa3')
    rDict = r.json()
    max = rDict.get('main').get('temp_max')
    return (f'La temperatura máxima actual en {city} es de {max} Cº')

def tempMin(city):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=sp,es&appid=8803b5791abaa43c513206e31d9cdaa3')
    rDict = r.json()
    min = rDict.get('main').get('temp_min')
    return (f'La temperatura mínima actual en {city} es de {min} Cº')

def weatherForecast(city):
    r = requests.get('http://api.openweathermap.org/geo/1.0/direct?q=' + city + '&lang=sp,es&appid=4c43ee2439e84f7dbcead5c02afc3ecf')
    rDict = r.json()
    cityLat = str(rDict[0]['lat'])
    cityLon = str(rDict[0]['lon'])
    r2 = requests.get('http://api.openweathermap.org/data/2.5/onecall?lat=' + cityLat + '&lon=' + cityLon + '&exclude=minutely,hourly,alerts&units=metric&lang=sp,es&appid=8803b5791abaa43c513206e31d9cdaa3')
    rDict2 = (r2.json().get('daily'))
    max = []
    min = []
    for day in rDict2:
        min.append(((day.get('temp')).get('min')))
        max.append(((day.get('temp')).get('max')))
    min.pop(0)
    max.pop(0)

    return (f'La media de la temperatura máxima para los próximos 7 días en {city} será de {round(statistics.mean(max), 2)} Cº\n'
            f'La media de la temperatura mínima para los próximos 7 días en {city} será de {round(statistics.mean(min), 2)} Cº')


print(tempMax('Londres'))
print(tempMin('Londres'))
print(weatherForecast('Londres'))

if __name__ == '__main__':
    main()
