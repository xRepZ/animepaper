import minio
from animepaper.settings import S3_MINIO
from . import object
from django.core.exceptions import BadRequest
import logging

logger = logging.getLogger(__name__)


class Minio:
    def __init__(self) -> None:
        self.client = minio.Minio(
        '%s:%s' % (S3_MINIO['HOST'], S3_MINIO['PORT']),
        access_key = S3_MINIO['MINIO_ACCESS_KEY'],
        secret_key = S3_MINIO['MINIO_SECRET_KEY'],
        secure = S3_MINIO['SECURE'],
    )

    def getObject(self, name: str) -> object.Object:
        try:
            response = self.client.get_object(S3_MINIO['BUCKET'], name)
        except Exception:
            raise SystemError
        finally:
            response.close()
            response.release_conn()

        if response.status != 200:
            raise SystemError
        
        logger.info(response)

        return object.Object('', response.getheader("content-type"), response.data)

    def setObject(self, obj : object.Object) -> None:
        if obj.name == '':
            raise BadRequest
    
        try:
            self.client.put_object(S3_MINIO['BUCKET'], obj.name, obj.body, len(obj.body.getvalue()), obj.contentType)
        except Exception as e:
            logger.info(e)
            raise SystemError
            
