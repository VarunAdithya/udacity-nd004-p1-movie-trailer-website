import json
import re
import urllib2


class Movie():
	'''A data structure to store my favorite movies'''

	VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

        def __init__(self, title, poster_image_url, trailer_youtube_url, imdb_url):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.imdb_url = imdb_url


class OMDbMovie(Movie):
    '''
    Data structure based on Movie class, with additional data from OMDb. To
    retrieve this data the API of the Open Movie Database will be used, which
    can be found at http://www.omdbapi.com/.

    Data from OMDb is JSON-encoded, and has these attributes:
    Title, Year, Rated, Released, Runtime, Genre, Director, Writer, Actors,
    Plot, Language, Country, Awards, Poster, Metascore, imdbRating, imdbVotes,
    imdbID, Type and Response
    '''

    OMDB_BASEURL = 'http://www.omdbapi.com/?i='

    def __init__(self, imdb_url, youtube_trailer):
        '''
        Initialize a Movie object with OMDb info retrieved from the OMDb API.
        '''
        self.imdb_id = self.url_to_id(imdb_url)
        self.imdb_url = imdb_url
        self.trailer_youtube_url= youtube_trailer
        self.query_omdb(self.imdb_id)
        Movie.__init__(self, self.omdb_json['Title'], self.omdb_json['Poster'], youtube_trailer, imdb_url)

    def url_to_id(self, url):
        '''
        Extract IMDb ID from the URL provided
        For a URL like http://www.imdb.com/title/tt1375666/ it should return tt1375666
        '''
        pattern = re.compile(r'tt[0-9]{7}')
        match = re.search(pattern, url)
        imdbID = match.group()
        return imdbID

    def query_omdb(self, imdbID):
        '''Get OMDb info about movie'''
        response = urllib2.urlopen(self.OMDB_BASEURL + imdbID)
        self.omdb_json = json.load(response)
