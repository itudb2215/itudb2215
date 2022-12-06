class Game:
    def __init__(self, title, game_id, year=None, image_url=None):
        self.title = title
        self.game_id = game_id
        self.release_year = year
        self.image_url = image_url
        