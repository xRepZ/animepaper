import io

class Object:
    def __init__(self, name: str, contentType: str, body: io.BytesIO) -> None:
        self.contentType = contentType
        self.body = body
        self.name = name