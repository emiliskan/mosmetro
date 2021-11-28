from datetime import datetime

from pydantic import BaseModel


class NewsModel(BaseModel):
    id: int
    caption: str
    date: datetime
    image_src: str
    scarp_date: datetime
