import fresh_tomatoes
import media


starwars_iv = media.OMDbMovie('http://www.imdb.com/title/tt0076759/',
        'https://www.youtube.com/watch?v=vZ734NWnAHA')

princess_mononoke = media.OMDbMovie('http://www.imdb.com/title/tt0119698/',
        'https://www.youtube.com/watch?v=4OiMOHRDs14')

flags_of_our_fathers = media.OMDbMovie('http://www.imdb.com/title/tt0418689/',
        'https://www.youtube.com/watch?v=1KiBildlym4')

the_dark_knight = media.OMDbMovie('http://www.imdb.com/title/tt0468569/',
        'https://www.youtube.com/watch?v=EXeTwQWrcwY')

letters_from_iwo_jima = media.OMDbMovie('http://www.imdb.com/title/tt0498380/',
        'https://youtu.be/U6rUr0mKwhc')

inception = media.OMDbMovie('http://www.imdb.com/title/tt1375666/',
        'https://www.youtube.com/watch?v=8hP9D6kZseM')

zwartboek = media.OMDbMovie('http://www.imdb.com/title/tt0389557/',
        'https://www.youtube.com/watch?v=DIklvGsU7bM')

ponyo = media.OMDbMovie('http://www.imdb.com/title/tt0876563/',
        'https://www.youtube.com/watch?v=CsR3KVgBzSM')

favorites = [princess_mononoke, flags_of_our_fathers, zwartboek, the_dark_knight, inception, letters_from_iwo_jima, starwars_iv, ponyo]

fresh_tomatoes.open_movies_page(favorites)
