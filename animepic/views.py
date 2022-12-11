from http.client import HTTPException
from .services.picture_getter import PictureDownloader
from django.views import View
from django.http import HttpResponse, HttpResponseServerError
from .services.image import Image
import logging


logger = logging.getLogger(__name__)

class PictureView(View):
    def __init__(self) -> None:
        self.downloader = PictureDownloader()
        
    def get(self, request, *args, **kwargs):
        image = Image('', bytearray(b''))
        try:
            image = self.downloader.getPicture()
        except HTTPException:
            HttpResponseServerError()
 
        logger.info("image proccessed successfully")
        return HttpResponse(image.body, content_type=image.contentType)




