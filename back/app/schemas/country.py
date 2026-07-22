from pydantic import BaseModel


class CountryResponse(BaseModel):
    id: int
    name: str
    iso3: str

    class Config:
        from_attributes = True
``