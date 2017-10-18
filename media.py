import webbrowser
class Movie():
    def __init__(self, movie_title, story_line, movie_image, movie_show_trailer):
        self.title = movie_title
        self.storyline = story_line
        self.poster_image_url = movie_image
        self.trailer_youtube_url = movie_show_trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
