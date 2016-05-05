# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

lord_of_the_rings_1 = media.Movie("Lord of the Rings - The Fellowship Of The Ring",
	"A hobbit learns that his magic ring is the key to saving Middle Earth from the Dark Lord",
	#source: "http://www.advancedfictionwriting.com/blog/2009/01/01/star-wars-one-sentence-summary/")
	"https://upload.wikimedia.org/wikipedia/en/0/0c/The_Fellowship_Of_The_Ring.jpg",
	"https://www.youtube.com/watch?v=Pki6jbSbXIY")

lord_of_the_rings_2 = media.Movie("Lord of the Rings - The Two Towers",
	"A hobbit learns that his magic ring is the key to saving Middle Earth from the Dark Lord",
	#source: "http://www.advancedfictionwriting.com/blog/2009/01/01/star-wars-one-sentence-summary/")
	"https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg",
	"https://www.youtube.com/watch?v=2dlRvAjU_RI")

lord_of_the_rings_3 = media.Movie("Lord of the Rings - The Return of the King",
	"A hobbit learns that his magic ring is the key to saving Middle Earth from the Dark Lord",
	#source: "http://www.advancedfictionwriting.com/blog/2009/01/01/star-wars-one-sentence-summary/")
	"https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
	"https://www.youtube.com/watch?v=r5X-hFf6Bwo")

hobbit_1 = media.Movie("The Hobbit - An Unexpected Journey",
	"The Hobbit is an adventure story involving Bilbo Baggins, a Hobbit, Gandalf, a wizard and several other creatures including dwarves, elves, and a dragon.",
	#source: "http://www.enotes.com/homework-help/short-summary-book-77385")
	"https://upload.wikimedia.org/wikipedia/en/b/b3/The_Hobbit-_An_Unexpected_Journey.jpeg",
	"https://www.youtube.com/watch?v=eI3f4b-b8ig")

hobbit_2 = media.Movie("The Hobbit - The Desolation of Smaug",
	"The Hobbit is an adventure story involving Bilbo Baggins, a Hobbit, Gandalf, a wizard and several other creatures including dwarves, elves, and a dragon.",
	#source: "http://www.enotes.com/homework-help/short-summary-book-77385")
	"https://upload.wikimedia.org/wikipedia/en/4/4f/The_Hobbit_-_The_Desolation_of_Smaug_theatrical_poster.jpg",
	"https://www.youtube.com/watch?v=fnaojlfdUbs")

hobbit_3 =  media.Movie("The Hobbit - The Battle of the Five Armies",
	"The Hobbit is an adventure story involving Bilbo Baggins, a Hobbit, Gandalf, a wizard and several other creatures including dwarves, elves, and a dragon.",
	#source: "http://www.enotes.com/homework-help/short-summary-book-77385")
	"https://upload.wikimedia.org/wikipedia/en/0/0e/The_Hobbit_-_The_Battle_of_the_Five_Armies.jpg",
	"https://www.youtube.com/watch?v=ZSzeFFsKEt4")

movies = [lord_of_the_rings_1, lord_of_the_rings_2, lord_of_the_rings_3, hobbit_1, hobbit_2, hobbit_3]
fresh_tomatoes.open_movies_page(movies)