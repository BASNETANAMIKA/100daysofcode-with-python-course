from collections import namedtuple,defaultdict

import csv
from urllib.request import  urlretrieve

url = "https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv"
movies_csv = 'movie_metadata.csv'
urlretrieve(url, 'movie_metadata.csv')
#### Movie namedtuple
Movie = namedtuple('Movie',['title', 'year','score'])


def get_movies_by_director(data = movies_csv):
    directors = defaultdict(list)
    with open(data) as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


directors=get_movies_by_director()
