from .api import WallpapersCraftAPI
from aiohttp import ClientSession
from bs4 import BeautifulSoup
from typing import List
from .types import Picture, TAG, RESOLUTIONS, CATALOG


class AsyncWallpapersCraftAPI(WallpapersCraftAPI):
    """Async API for wallpaperscraft.com"""

    async def get(self, query: str = "/", **kwargs):
        if not query.startswith(self.WEBSITE):
            query = self.WEBSITE + query
        
        async with ClientSession() as session:
            responce = await session.get(query, **kwargs)
            if not responce.raise_for_status():
                return BeautifulSoup(await responce.text())
    
    async def get_wallpaper(self, link: str):
        return (await self.get(link)).find("img", {"class": "wallpaper__image"}).get("src")

    async def all(self, page: int = 1, resolution: str = "") -> List[Picture]:
        """All pictures."""
        if resolution:
            if resolution not in RESOLUTIONS:
                raise ValueError("Parameter <resolution> isn't a valid screen resolution! Please set a valid resolution.")
            resolution = "/" + resolution
        
        return self.get_all_pictures_from_page(await self.get(f"/all{resolution}/page{page}"))
    
    async def get_by_tag(self, tag: TAG, page: int = 1, resolution: str = ""):
        """Get pictures by tag and page"""

        if type(tag) != TAG:
            raise TypeError("Parameter tag should be a value from wallpaperscraft.TAG")
        
        if resolution:
            if resolution not in RESOLUTIONS:
                raise ValueError("Parameter <resolution> isn't a valid screen resolution! Please set a valid resolution.")
            resolution = "/" + resolution
        
        return self.get_all_pictures_from_page(await self.get(f"/tag/{tag.value}{resolution}/page{page}"))
    
    async def get_by_catalog(self, catalog: CATALOG, page: int = 1, resolution: str = ""):
        """Get pictures by catalog and page"""

        if type(catalog) != CATALOG:
            raise TypeError("Parameter tag should be a value from wallpaperscraft.CATALOG")
        
        if resolution:
            if resolution not in RESOLUTIONS:
                raise ValueError("Parameter <resolution> isn't a valid screen resolution! Please set a valid resolution.")
            resolution = "/" + resolution
        
        return self.get_all_pictures_from_page(await self.get(f"/catalog/{catalog.value}{resolution}/page{page}"))
    
    async def search(self, query: str, page: int = 1, resolution: str = ""):
        """Get pictures by search query and page"""
        if resolution and resolution not in RESOLUTIONS:
            raise ValueError("Parameter <resolution> isn't a valid screen resolution! Please set a valid resolution.")

        return self.get_all_pictures_from_page(
            await self.get(
                "https://wallpaperscraft.com/search/",
                params={
                    "order": "",
                    "page": str(page),
                    "query": query.strip().replace(" ", "+"),
                    "size": resolution
                }
            )
        )
