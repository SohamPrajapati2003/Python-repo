movies = [
    {"movie_id": 1, "title": "Inception", "genre": "Sci-Fi", "rating": 8.8},
    {"movie_id": 2, "title": "Titanic", "genre": "Romance", "rating": 7.8},
    {"movie_id": 3, "title": "Avengers", "genre": "Action", "rating": 8.5},
    {"movie_id": 4, "title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6},
    {"movie_id": 5, "title": "The Notebook", "genre": "Romance", "rating": 7.9}
]

movie_title = []


for i in movies:
    if 'genre' in i:
        # print("hi")
        if i["genre"] == 'Sci-Fi':
            print(i['title'])


