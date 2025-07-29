class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

mov1 = Movie("qasoskorlar", "action", 120, 8.5)
print(mov1.title)
print(mov1.genre)   
print(mov1.duration)
print(mov1.rating)