# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
	"A story of a boy and his toys that come to life",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
	"A marine on an alien planet",
	"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")

lord_of_the_rings = media.Movie("Lord of the Rings",
	"A hobbit learns that his magic ring is the key to saving Middle Earth from the Dark Lord",
	#source: "http://www.advancedfictionwriting.com/blog/2009/01/01/star-wars-one-sentence-summary/")
	"http://vignette3.wikia.nocookie.net/lotr/images/7/74/LOTRFOTRmovie.jpg/revision/latest?cb=20150203040819",
	"https://www.youtube.com/watch?v=V75dMMIW2B4")

school_of_rock = media.Movie("School of Rock",
	"Using rock music to learn",
	"http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
	"https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
	"A rat is a chef in Paris",
	"http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
	"https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
	"Going back in time to meet authors",
	"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
	"https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("Hunger Games",
	"A really real reality show",
	"https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
	"https://www.youtube.com/watch?v=SMGRhAEn6K0")

#print(lord_of_the_rings.storyline)
#lord_of_the_rings.show_trailer()

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)