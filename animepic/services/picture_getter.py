from http.client import HTTPException
import requests
from . import image
from typing import List


class PictureDownloader:
    URL = "https://pic.re/image"

    def getPicture(self) -> image.Image:
        resp = requests.get(url=self.URL)
        if resp.status_code != 200:
            raise HTTPException

        return image.Image(resp.headers['content-type'], resp.content)