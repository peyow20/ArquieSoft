import csv
import re

# Principio de Solid OCP: El archivo se encarga de varios modulos, pero si se quiere agregar otra funcionalidad, no va a ser necesario
# modificar el codigo

def movie_formatter(movies, links, crew, ratings, votes):
    # Create a empty list for storing
    # movie information
    list = []

    # Iterating over movies to extract
    # each movie's details
    for index in range(0, len(movies)):
        # Separating movie into: 'place',
        # 'title', 'year'
        movie_string = movies[index].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(index)) + 1:-7]
        year = re.search('\((.*?)\)', movie_string).group(1)
        place = movie[:len(str(index)) - (len(movie))]

        data = {"movie_title": movie_title,
                "year": year,
                "place": place,
                "star_cast": crew[index],
                "rating": ratings[index],
                "vote": votes[index],
                "link": links[index],
                "preference_key": index % 4 + 1}

        list.append(data)
    return list


def csv_writer(fields: list, list: list, file_name: str):
    with open(file_name, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for element in list:
            writer.writerow({**element})
