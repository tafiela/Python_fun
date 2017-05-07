
'''
every movie has a :

title
storyline
poster_image
trailer

'''

import webbrowser


class Movie():
    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer): #class constructor, it creates a memory instance for an object
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
    
    def show_trailer(self):
        mv_trailer= webbrowser.open(self.trailer_youtube_url)
        