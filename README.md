# udacity-nd004-p1-movie-trailer-website

This code is the result I achieved for ***[Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/course/nd004) - Project 1: Movie Trailer Website***.

This code has been *reviewed by me*. According to me, based on the rubric used by the Udacity reviewer, this code:
- [x] Exceeds Specifications: Student includes additional information about their favorite movies (actors, release date, etc) or personalizes their page with additional HTML or CSS features.
- [x] Meets Specifications: Page is dynamically generated from a Python data structure.
- [x] Meets Specifications: Page is error free.
- [x] Meets Specifications: Code is ready for personal review and neatly formatted.
- [x] Meets Specifications: Comments are present.
- [x] Exceeds Specifications: Comments are thorough and concise. Code is self documenting.
- [x] Meets Specifications: A README file is included. README file includes details of all the steps required to successfully run the application.

A list of websites, books, forums, blog posts, Github repositories etcetera that I have referred to or used in this submission can be found in the [references.txt](https://github.com/swesterveld/udacity-nd004-p1-movie-trailer-website/references.txt) file.

## Fresh Tomatoes Movie Trailers
This code is based on the Python module called [fresh_tomatoes.py](https://s3.amazonaws.com/udacity-hosted-downloads/ud036/fresh_tomatoes.py) provided in Udacity's course about [Programming Foundations with Python](https://www.udacity.com/course/ud036). There are several things I've added to (or modified in) this module:
1. The movie-tiles now all have similar height, resulting in rows filled with movie-tiles starting from the left. This has been achieved by making sure the title will be rendered on a single line (with an ellipsis if needed), and reserving 4 lines of space for the plot (and limit its word-count if needed).
2. Each movie-tile has a block with additional information from the [Open Movie Database](http://www.omdb.com/): release date, director, plot, rating on [IMDb](http://www.imdb.com/) and metascore on [Metacritic](http://www.metacritic.com/).
3. For every movie with an [MPAA film rating](http://en.wikipedia.org/wiki/Motion_Picture_Association_of_America_film_rating_system) (in OMDb), the rating symbol is rendered as an overlay on the movie-poster. Assets for the rating symbols have been downloaded from Wikipedia.
4. And more...

A module with classes for the movies can be found in [media.py](https://github.com/swesterveld/udacity-nd004-p1-movie-trailer-website/blob/master/media.py), which has a generic Movie-class based on the one used in Udacity's course about [Programming Foundations with Python](https://www.udacity.com/course/ud036). For all the OMDb-related information, I have added an OMDbMovie-class which extends the Movie-class.

## Run the application
1. Make sure Python and Git have been installed on your computer
2. Make sure your computer is connected to the internet
2. Clone this repository to a directory on your computer
3. Run ```python mediacenter.py```, wait for a little moment, and the website will be opened in your webbrowser
