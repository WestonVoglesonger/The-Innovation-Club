from pydantic import BaseModel, HttpUrl

class ProductData(BaseModel):
    id: int | None
    name: str
    description: str
    url: str