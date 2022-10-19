from bs4 import BeautifulSoup
from Movie_connection import url_connection
from movie_format import csv_writer, movie_format

# Principios de Solid ISP: Solo de usan metodos que estan declarados y cumplen con una funcionalidad en el codigo

def main():

    # Downloading imdb top 250 movie's data
    url = 'http://www.imdb.com/chart/top'
    response = url_connection(url)
    soup = BeautifulSoup(response.text, 'lxml')

    movies = soup.select('td.titleColumn')
    links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
    votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

    # create a empty list for storing
    # movie information

    movies = movie_format(movies, links, crew, ratings, votes)
    filename = "movie_results.csv"
    fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
    csv_writer(fields, movies, filename)

if __name__ == '__main__':
    main()
