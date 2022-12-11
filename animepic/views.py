from http.client import HTTPException
import uuid
from .services.pictureDownloader import PictureDownloader
from django.views import View
from django.http import HttpResponse, HttpResponseServerError
from .services.image import Image
from common.s3 import minio, object
import logging
import mimetypes
import io


logger = logging.getLogger(__name__)

class PictureView(View):
    def __init__(self) -> None:
        self.downloader = PictureDownloader()
        self.minio = minio.Minio()
        
    def get(self, request, *args, **kwargs):
        #image = Image('', bytearray(b''))
        try:
            image = self.downloader.getPicture()
        except HTTPException:
            logger.error("can't get pic")
            return HttpResponseServerError()

        try:
            self.minio.setObject(object.Object(
                str(uuid.uuid4()) + mimetypes.guess_extension(image.contentType),
                image.contentType,
                io.BytesIO(image.body)))
        except SystemError:
            logger.error("can't set minio")
            return HttpResponseServerError()
 
        logger.info("image proccessed successfully")
        return HttpResponse(image.body, content_type=image.contentType)




