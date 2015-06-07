""" The Udacity project, movie trailer project, that is done by Wei-Chung Chen"""

import webbrowser

#create movie class and define the constructor that is for creating specific instance

class Movie(): 

     def __init__(self, title, description, release_year, poster_image, trailer_youtube_url):
       self.title= title
       self.description= description
       self.release_year= release_year
       self.poster_image_url= poster_image
       self.trailer_youtube_url=  trailer_youtube_url
       
# define a method that can show video on web       
     def show_trailer(self):
       webbrowser.open(self.movie_trailer_url)