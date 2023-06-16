# WallpapersCraftAPI
> Unofficial API WallpapersCraft (wallpaperscraft.com)

#
# <img width="30" height="30" src="https://img.icons8.com/external-sbts2018-outline-color-sbts2018/58/external-install-basic-ui-elements-2.3-sbts2018-outline-color-sbts2018.png" alt="external-install-basic-ui-elements-2.3-sbts2018-outline-color-sbts2018"/> Install

## Install via GitHub:
``` bash
pip3 install https://github.com/Den4ikSuperOstryyPer4ik/WallpapersCraftAPI/archive/main.zip --upgrade
```

## Stable version from PyPi:
``` bash
pip3 install wallpaperscraft
```
> For Windows: <s>pip3</s> > <b>pip</b>

# Usage

``` python
from wallpaperscraft import WallpapersCraftAPI, TAG, CATALOG

api = WallpapersCraftAPI()

# get 15 pictures from first page with nature by size 1024x768
nature_pics = api.get_by_catalog(CATALOG.NATURE, resolution="1024x768")

# get 15 pictures from 5th(fifth) page with space by size 1920x1080
vectore_pics = api.get_by_catalog(CATALOG.SPACE, page=5, resolution="1920x1080")

# get 15 pictures from second(2) page with sky and different size
sky_pictures = api.get_by_tag(TAG.SKY, page=2)

# search pictures from first page with night city and different size
night_city_pics = api.search("night city")

# get 15 pictures from first page on `https://wallpaperscraft.com/all/` by different size
all_pics = api.all()
```

# Async Usage
``` python
from wallpaperscraft import AsyncWallpapersCraftAPI, TAG, CATALOG
import asyncio

async def main():
    api = AsyncWallpapersCraftAPI()

    # get 15 pictures from first page with nature by size 1024x768
    nature_pics = await api.get_by_catalog(CATALOG.NATURE, resolution="1024x768")

    # get 15 pictures from 5th(fifth) page with space by size 1920x1080
    vectore_pics = await api.get_by_catalog(CATALOG.SPACE, page=5, resolution="1920x1080")

    # get 15 pictures from second(2) page with sky and different size
    sky_pictures = await api.get_by_tag(TAG.SKY, page=2)

    # search pictures from first page with night city and different size
    night_city_pics = await api.search("night city")

    # get 15 pictures from first page on `https://wallpaperscraft.com/all/` by different size
    all_pics = await api.all()

asyncio.run(main())
```