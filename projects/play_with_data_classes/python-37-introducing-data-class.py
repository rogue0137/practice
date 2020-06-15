# Jetbrains tutorial on Python 3.7 Data Classes
# https://blog.jetbrains.com/pycharm/2018/04/python-37-introducing-data-class
import requests
import dateutil
import datetime

response = requests.get('https://swapi.co/api/films/1')

#dictionary = response.json()
#print(dictionary)


# not use dataclass; not DRY
class StarWarsMovie:

    def __init__(self,
                 title: str,
                 episode_id: int,
                 opening_crawl: str,
                 director: str,
                 producer: str,
                 release_date: datetime,
                 characters: List[str],
                 planets: List[str],
                 starships: List[str],
                 vehicles: List[str],
                 species: List[str],
                 created: datetime,
                 edited: datetime,
                url: str
                 ):

    self.title = title
    self.episode_id = episode_id
    self.opening_crawl = opening_crawl
    self.director = director
    self.producer = producer
    self.release_date = release_ddate
    self.characters = characters
    self.planets = planets
    self.starships = starships
    self.species = species
    self.created = created
    self.edited = edited
    self.url = url

    if type(self.release_date) is str:
        self.release_date = dateutil.parser.parse(self.release_date)

    if type(self.created) is str:
        self.created = dateutil.parser.parse(self.created)

    if type(self.edited) is str:
        self.edited = dateutil.parser.parse(self.edited)

# using dataclass

@dataclass
class StarWarsMovie:
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date: datetime
    characters: List[str]
    planets: List[str]
    starships: List[str]
    vehicles: List[str]
    species: List[str]
    created: datetime
    edited: datetime
    url: str

    def __post_init__(self):
        if type(self.release_date) is str:
            self.release_date = dateutil.parser.parse(self.release_date)

        if type(self.created) is str:
            self.created = dateutil.parser.parse(self.created)

        if type(self.edited) is str:
            self.edited = dateutil.parser.parse(self.edited)



