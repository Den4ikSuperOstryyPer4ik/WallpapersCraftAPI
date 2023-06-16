from bs4 import BeautifulSoup
from typing import List
from requests import get
from .types import Picture, TAG, CATALOG, RESOLUTIONS


class WallpapersCraftAPI:
    """Sync API for wallpaperscraft.com"""

    WEBSITE = "https://wallpaperscraft.com"
    
    def get(self, query: str = "/", **kwargs):
        if not query.startswith(self.WEBSITE):
            query = self.WEBSITE + query
        
        responce = get(query, **kwargs)
        if not responce.raise_for_status():
            return BeautifulSoup(responce.text, "html.parser")
    
    def get_all_pictures_from_page(self, page: BeautifulSoup):
        return [
            Picture(
                link=self.WEBSITE + pic.find("a", {"class": "wallpapers__link"}).get("href"),
                info=pic.find("a", {"class": "wallpapers__link"}).find_all("span", {"class": "wallpapers__info"})[1].text,
                downloads=pic.find("a", {"class": "wallpapers__link"}).find_all("span", {"class": "wallpapers__info"})[0].find("span", {"class": "wallpapers__info-downloads"}).text,
                rating=pic.find("a", {"class": "wallpapers__link"}).find_all("span", {"class": "wallpapers__info"})[0].find("span", {"class": "wallpapers__info-rating"}).text.strip(),
                api_class=self
            )
            for pic in page.find_all("li", {"class": "wallpapers__item"})
        ]

    def get_wallpaper(self, link: str):
        return self.get(link).find("img", {"class": "wallpaper__image"}).get("src")

    def all(self, page: int = 1, resolution: str = "") -> List[Picture]:
        """All pictures."""
        if resolution:
            if resolution not in RESOLUTIONS:
                raise ValueError("Parameter <resolution> isn't a valid screen resolution! Please set a valid resolution.")
            resolution = "/" + resolution
        
        return self.get_all_pictures_from_page(self.get(f"/all{resolution}/page{page}"))
    
    def get_by_tag(self, tag: TAG, page: int = 1, resolution: str = ""):
        """Get pictures by tag and page"""

        if type(tag) != TAG:
            raise TypeError("Parameter tag should be a value from wallpaperscraft.TAG")
        
        if resolution:
            if resolution not in RESOLUTIONS:
                raise ValueError("Parameter <resolution> isn't a valid screen resolution! Please set a valid resolution.")
            resolution = "/" + resolution
        
        return self.get_all_pictures_from_page(self.get(f"/tag/{tag.value}{resolution}/page{page}"))
    
    def get_by_catalog(self, catalog: CATALOG, page: int = 1, resolution: str = ""):
        """Get pictures by catalog and page"""

        if type(catalog) != CATALOG:
            raise TypeError("Parameter tag should be a value from wallpaperscraft.CATALOG")
        
        if resolution:
            if resolution not in RESOLUTIONS:
                raise ValueError("Parameter <resolution> isn't a valid screen resolution! Please set a valid resolution.")
            resolution = "/" + resolution
        
        return self.get_all_pictures_from_page(self.get(f"/catalog/{catalog.value}{resolution}/page{page}"))
    
    def search(self, query: str, page: int = 1, resolution: str = ""):
        """Get pictures by search query and page"""
        if resolution and resolution not in RESOLUTIONS:
            raise ValueError("Parameter <resolution> isn't a valid screen resolution! Please set a valid resolution.")

        return self.get_all_pictures_from_page(
            self.get(
                "https://wallpaperscraft.com/search/",
                params={
                    "order": "",
                    "page": str(page),
                    "query": query.strip().replace(" ", "+"),
                    "size": resolution
                }
            )
        )


