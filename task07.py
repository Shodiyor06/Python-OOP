class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

    def show_summary(self):
        print(f"{self.title} — {self.genre} janridagi film. Reyting: {self.rating}/10.")

film1 = Movie("Inception", "fantastika", 148, 8.8)
film2 = Movie("Titanic", "romantik drama", 195, 7.9)

film1.show_summary()  
film2.show_summary() 