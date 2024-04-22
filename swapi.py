import requests

# Función para hacer solicitudes a la API de SWAPI
def get_data(url):
    response = requests.get(url, verify=False)  # Ignorar la verificación del certificado SSL
    if response.status_code == 200:
        return response.json()
    else:
        return None

# a) Contar el número de películas en las que aparecen planetas con clima árido
def count_arid_planet_films():
    films = get_data('https://swapi.dev/api/films/')
    if films:
        arid_planet_films = [film for film in films['results'] if 'climate' in film and 'arid' in film['climate']]
        return len(arid_planet_films)
    else:
        return None


# b) Contar el número de personajes de tipo "Wookiee"
def count_wookie_characters():
    wookies = get_data('https://swapi.dev/api/species/3/')
    if wookies:
        return wookies['people']
    else:
        return None

# c) Encontrar la aeronave más pequeña en la primera película
def find_smallest_ship():
    film_1 = get_data('https://swapi.dev/api/films/1/')
    if film_1:
        starships = film_1.get('starships', [])
        if starships:
            smallest_ship = min(starships, key=lambda x: int(x.split('/')[-2]))  # Utiliza la ID de la nave para comparar la longitud
            ship_data = get_data(smallest_ship)
            if ship_data:
                return ship_data['name']
    return None


# Ejemplo de uso:
print("a) Número de películas con planetas de clima árido:", count_arid_planet_films())
print("b) Número de personajes de tipo Wookiee:", len(count_wookie_characters()))
print("c) Aeronave más pequeña en la primera película:", find_smallest_ship())
