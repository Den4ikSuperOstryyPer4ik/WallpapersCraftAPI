from typing import Optional, Any
from pydantic import BaseModel
from enum import Enum


RESOLUTIONS = [
    "1920x1080",
    "240x320",
    "240x400",
    "320x240",
    "320x480",
    "360x640",
    "480x800",
    "480x854",
    "540x960",
    "720x1280",
    "800x600",
    "800x1280",
    "960x544",
    "1024x600",
    "1080x1920",
    "2160x3840",
    "1366x768",
    "1440x2560",
    "800x1200",
    "800x1420",
    "938x1668",
    "1280x1280",
    "1350x2400",
    "3415x3415",
    "2780x2780",
    "1024x768",
    "1152x864",
    "1280x960",
    "1400x1050",
    "1600x1200",
    "1280x1024",
    "1280x720",
    "1280x800",
    "1440x900",
    "1680x1050",
    "1920x1200",
    "2560x1600",
    "1600x900",
    "2560x1440",
    "2048x1152",
    "2560x1024",
    "2560x1080",
    "3840x2400",
    "3840x2160",
]


class Picture(BaseModel):
    link: str
    info: str
    downloads: int
    rating: Optional[str] = None
    api_class: Any

    def download(self, resolution: str = "1024x768"):
        """
        Get link for picture by resolution
        """
        if resolution not in RESOLUTIONS:
            raise ValueError("Parameter <resolution> isn't a valid screen resolution! Please set a valid resolution.")
        URL = f"{self.link.replace('/wallpaper/', '/download/')}"
        if not any(URL.endswith(i) for i in RESOLUTIONS):
            URL += f"/{resolution}"
        return self.api_class.get_wallpaper(URL)


class CATALOG(Enum):
    _3D = "3d"
    ABSTRACT = "abstract"
    ANIMALS = "animals"
    ANIME = "anime"
    ART = "art"
    BLACK = "black"
    BLACK_AND_WHITE = "black_and_white"
    CARS = "cars"
    CITY = "city"
    DARK = "dark"
    FANTASY = "fantasy"
    FLOWERS = "flowers"
    FOOD = "food"
    HOLIDAYS = "holidays"
    LOVE = "love"
    MACRO = "macro"
    MINIMALISM = "minimalism"
    MOTORCYCLES = "motorcycles"
    MUSIC = "music"
    NATURE = "nature"
    OTHER = "other"
    SPACE = "space"
    SPORT = "sport"
    TECHNOLOGIES = "technologies"
    TEXTURES = "textures"
    VECTOR = "vector"
    WORDS = "words"


class TAG(Enum):
    ANGEL = "angel"
    ART = "art"
    ASTON_MARTIN = "aston martin"
    AUTUMN = "autumn"
    BLACK = "black"
    BLONDE = "blonde"
    BRUNETTE = "brunette"
    BUGATTI = "bugatti"
    CAT = "cat"
    DOG = "dog"
    DRAGON = "dragon"
    FERRARI = "ferrari"
    FUNNY = "funny"
    GALAXY = "galaxy"
    HEART = "heart"
    KITTEN = "kitten"
    LAMBORGHINI = "lamborghini"
    LION = "lion"
    LOVE = "love"
    MINIMALISM = "minimalism"
    OWL = "owl"
    PUPPY = "puppy"
    ROBOT = "robot"
    ROSE = "rose"
    SEA = "sea"
    SKY = "sky"
    SPRING = "spring"
    STARS = "stars"
    SUMMER = "summer"
    SUN = "sun"
    TIGER = "tiger"
    WHITE = "white"
    WINTER = "winter"
    WOLF = "wolf"
    ZOMBIE = "zombie"
