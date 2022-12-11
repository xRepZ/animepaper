class Image:
    def __init__(self, contentType: str, body: bytearray) -> None:
        self.contentType = contentType
        self.body = body

    def getBody(self)->bytearray:
        return self.body

