class Movie:
    def __init__(self, movie_name, rating):
        self.movie_name = movie_name
        self.rating = rating
    def display_movie(self):
        print("Movie:", self.movie_name)
        print("Rating:", self.rating, "/ 5")
movie = Movie("Inception", 4.8)
movie.display_movie()