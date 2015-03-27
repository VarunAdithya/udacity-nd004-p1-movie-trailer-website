import json
import re
import urllib2
import datetime


class Movie():
    '''A data structure to store my favorite movies'''

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R', 'NC-17']

    def __init__(self, title, poster_image_url, trailer_youtube_url, imdb_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.imdb_url = imdb_url


class OMDbMovie(Movie):
    '''
    Data structure based on Movie class, with additional data from OMDb. To
    retrieve this data the API of the Open Movie Database (OMDb) is being used.
    OMDb can be found at http://www.omdbapi.com/.

    Data from OMDb is JSON-encoded, and has these attributes:
    Title, Year, Rated, Released, Runtime, Genre, Director, Writer, Actors,
    Plot, Language, Country, Awards, Poster, Metascore, imdbRating, imdbVotes,
    imdbID, Type and Response
    '''

    # Base URL to get information from the OMDb API, based on the
    # IMDb ID of the movie.
    OMDB_BASEURL = 'http://www.omdbapi.com/?i='

    # Dictionary of asset-locations for MPAA film-rating symbols.
    OMDB_RATING_ASSETS = {
            'G':     'img/RATED_G.svg',
            'PG':    'img/RATED_PG.svg',
            'PG-13': 'img/RATED_PG-13.svg',
            'R':     'img/RATED_R.svg',
            'NC-17': 'img/Nc-17.svg'
            }


    def __init__(self, imdb_url, youtube_trailer):
        '''
        Initialize a Movie object with OMDb info retrieved from the OMDb API.
        '''
        # Use the given IMDb URL to extract the IMDb ID and query the
        # OMDb API.
        self.imdb_id = self.get_imdb_id(imdb_url)
        self.imdb_url = imdb_url
        self.query_omdb(self.imdb_id)

        Movie.__init__(self, self.omdb['Title'], self.omdb['Poster'],
                youtube_trailer, imdb_url)

    def get_imdb_id(self, url):
        '''
        Extract IMDb ID from the URL provided
        For a URL like http://www.imdb.com/title/tt1375666/ it should return
        tt1375666
        '''
        # Looking for a string of 2 t-charachters, follwed by 7 digits.
        pattern = re.compile(r'tt[0-9]{7}')
        match = re.search(pattern, url)
        iid = match.group()
        return iid

    def get_release_date(self):
        '''
        Convert the date given by OMDb to a string with normal date notation.
        Date notations seen on OMDb are like '1977-05-05' or '12 Jul 1997'.
        '''
        # First try to figure out and save the date-format
        if '-' in self.omdb['Released']:
            fmt = '%Y-%m-%d'
        elif ' ' in self.omdb['Released']:
            fmt = '%d %b %Y'
        # Pass the date in OMDb notation if the format is unknown
        else:
            return self.omdb['Released']

        # Return a string with normal date notation, based on the year,
        # month and day we've extracted from the date given by OMDb.
        return datetime.datetime.strptime(self.omdb['Released'], fmt).strftime(
                '%B %d, %Y')

    def query_omdb(self, iid):
        '''Get OMDb info about movie, based on IMDb ID.'''
        # Open the URL on OMDb for the movie of the given IMDb ID.
        response = urllib2.urlopen(self.OMDB_BASEURL + iid)
        # Store the given movie-information as a dictionary
        self.omdb = json.load(response)

    def limit_plot(self, wc=20):
        '''
        Shorten the plot to a given word-count. If now word-count is given, a
        default of 20 words will be used.
        '''
        # First split the plot to a list of words
        split_plot = self.omdb['Plot'].split()

        # Return a string with the length of the given word-count and an
        # ellipsis if the full plot is longer.
        if len(split_plot) > wc:
            return unicode(' '.join(split_plot[:wc])) + ' &hellip;'
        else:
            return self.omdb['Plot']

    def get_rating_symbol(self):
        '''
        Get the location of the rating symbol image corresponding to the MPAA
        film-rating of the movie.
        '''
        if self.omdb['Rated'] in self.VALID_RATINGS:
            return self.OMDB_RATING_ASSETS[self.omdb['Rated']]
        else:
            return None
