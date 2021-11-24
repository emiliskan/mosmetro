from pydantic import BaseModel


class NewsModel(BaseModel):
    id: int
    caption: str
    date: str
    image_src: str
