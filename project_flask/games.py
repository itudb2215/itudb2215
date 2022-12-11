class Game:
    def __init__(self, _game_id, _query_name, _release_year=None, _required_age=None, _metacritic=None, _about_text=None, _image_url=None,
                 ):
        self.game_id = _game_id
        self.release_year = _release_year
        self.required_age = _required_age
        self.query_name = _query_name
        self.metacritic = _metacritic
        self.about_text = _about_text
        self.image_url = _image_url
        