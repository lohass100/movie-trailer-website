""" The Udacity project, movie trailer project, that is done by Wei-Chung Chen"""

#specify the file path to make sure we can import the file sucessfully
import sys
sys.path.append('/Users/Alan/Documents/Python/Movie_trailer_project')

#import files that will be used in the following process
import media_WeiChung
import fresh_tomatoes

#instance of movie trailer(mission impossible 5)
missionImpossible5 = media_WeiChung.Movie(
             "Mission Impossible 5",
             "A impossible mission need to be completed",
             "2015",
             "http://i.ytimg.com/vi/hxuAIqVNau4/hqdefault.jpg",
             "https://www.youtube.com/watch?v=pXwaKB7YOjw")

#instance of movie trailer(transformers)
transformers = media_WeiChung.Movie(
            "Transformers",
            "A story about many robots with humans",
            "2014",
            "http://screenrant.com/wp-content/uploads/sr-underground-150-tran"
            +"sformers-4-age-of-extinction.jpg",
            "https://www.youtube.com/watch?v=DkIPIkPPbdo")


#instance of movie trailer(avengers)
avengers = media_WeiChung.Movie(
            "Avengers",
            "It's a long story about many heros",
            "2015",
            "http://t0.gstatic.com/images?q=tbn:ANd9GcRlGeugacR"+
            "kKznDOtRhUCVt0AkrOTPbaaKwF9xgGZgNViyC_Xko",
            "https://www.youtube.com/watch?v=rD8lWtcgeyg")

terminators = media_WeiChung.Movie(
            "Terminators",
            "It's a exciting story about a human-like robot",
            "2015",
            "http://t1.gstatic.com/images?q=tbn:"+
            "ANd9GcSR2BVCGiBuW_mIdFXqPgxkxZU3N7AGhujf0SsiIyQpnsoq8QhW",
            "https://www.youtube.com/watch?v=jNU_jrPxs-0")


#put all the instance into a set of movie that are going to run in fresh_tomatoes
movies = [missionImpossible5, transformers, avengers, terminators]

#use open_movie_page method which is in the fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
