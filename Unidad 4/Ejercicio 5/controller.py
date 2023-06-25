import requests
import json
from models import Movie
from views import MovieViwer

class ManejadorMovie(object):
    def __init__(self):
        api_key = '41eae6fa38986e026b1f69902ee5bd08'
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}"
        response = requests.get(url)
        data = response.json()
        self.__movies = data["results"]
        self.__ManejadorPeliculas = []
        
    def Carga_Pelis(self):
        for movie in self.__movies:
            unaPelicula = Movie(movie["title"],movie["overview"],movie["original_language"],movie["release_date"])
            for idGen in movie["genre_ids"]:
                unaPelicula.Carga_Genero(idGen)
            self.__ManejadorPeliculas.append(unaPelicula) 

    def Busca_Generos(self,ids):
        data = {
            "genres": [
                {"id": 28, "name": "Action"},
                {"id": 12, "name": "Adventure"},
                {"id": 16, "name": "Animation"},
                {"id": 35, "name": "Comedy"},
                {"id": 80, "name": "Crime"},
                {"id": 99, "name": "Documentary"},
                {"id": 18, "name": "Drama"},
                {"id": 10751, "name": "Family"},
                {"id": 14, "name": "Fantasy"},
                {"id": 36, "name": "History"},
                {"id": 27, "name": "Horror"},
                {"id": 10402, "name": "Music"},
                {"id": 9648, "name": "Mystery"},
                {"id": 10749, "name": "Romance"},
                {"id": 878, "name": "Science Fiction"},
                {"id": 10770, "name": "TV Movie"},
                {"id": 53, "name": "Thriller"},
                {"id": 10752, "name": "War"},
                {"id": 37, "name": "Western"}
        ]
    }
        lista=[]
        for genre in data["genres"]:
            genre_id = genre["id"]
            for i in range(len(ids)):
                if ids[i] == genre_id:
                    lista.append(genre["name"])
                    
        return lista
            
    def getLista(self):
        return self.__ManejadorPeliculas
            
if __name__ == '__main__':
    menejador = ManejadorMovie()
    menejador.Carga_Pelis()
    app = MovieViwer(menejador)
    app.Ejecutar()