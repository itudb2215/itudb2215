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

class Additional:
    def __init__(self, _game_id, _background=None, _headerimage=None, _supporturl=None, _website=None, _recomendationcount=None, _steamspyowners=None, _steamspyplayersestimate=None
                 ):
                 
        self.game_id = _game_id
        self.background = _background
        self.headerimage = _headerimage
        self.supporturl = _supporturl
        self.website = _website
        self.recomendationcount = _recomendationcount
        self.steamspyowners = _steamspyowners
        self.steamspyplayersestimate = _steamspyplayersestimate
        
class Genre:
    def __init__(self, _game_id, _GenreIsNonGame=None, _GenreIsIndie=None, _GenreIsAction=None, _GenreIsAdventure=None, _GenreIsCasual=None, _GenreIsStrategy=None, _GenreIsRPG=None, _GenreIsSimulation=None, _GenreIsEarlyAccess=None, _GenreIsFreeToPlay=None,_GenreIsSports=None, _GenreIsRacing=None, _GenreIsMassivelyMultiplayer=None
                 ):
        self.game_id = _game_id
        self.GenreIsNonGame = _GenreIsNonGame
        self.GenreIsIndie = _GenreIsIndie
        self.GenreIsAction = _GenreIsAction
        self.GenreIsAdventure = _GenreIsAdventure
        self.GenreIsCasual = _GenreIsCasual
        self.GenreIsStrategy = _GenreIsStrategy
        self.GenreIsRPG = _GenreIsRPG
        self.GenreIsSimulation = _GenreIsSimulation
        self.GenreIsEarlyAccess = _GenreIsEarlyAccess
        self.GenreIsFreeToPlay = _GenreIsFreeToPlay
        self.GenreIsSports = _GenreIsSports
        self.GenreIsRacing = _GenreIsRacing
        self.GenreIsMassivelyMultiplayer = _GenreIsMassivelyMultiplayer

class Requirements:
    def __init__(self, _game_id, _response_id, _platformwindows=None, _platformlinux=None, _platformmac=None, _pcminreqtext=None, _linuxminreqtext=None, _macminreqtext=None, 
                 ):
        self.game_id = _game_id
        self.response_id = _response_id
        self.platformwindows = _platformwindows
        self.platformlinux = _platformlinux
        self.platformmac = _platformmac
        self.pcminreqtext = _pcminreqtext
        self.linuxminreqtext = _linuxminreqtext
        self.macminreqtext = _macminreqtext    



class Review:
    def __init__(self, _game_id, _review_id, _language=None, _review=None, _timestamp_created=None, _votes_helpful=None, _votes_funny=None, _recommended=None, _author_steam_id=None
                 ):
                 
        self.game_id = _game_id
        self.review_id = _review_id
        self.language = _language
        self.review = _review
        self.timestamp_created = _timestamp_created
        self.votes_helpful = _votes_helpful
        self.votes_funny = _votes_funny
        self.author_steam_id = _author_steam_id