from typing import List

from pydantic import BaseModel

class PinBase(BaseModel):
    pass

class PinRow(PinBase):
    pin: str
    place_name: str
    state: str
    longitude: float
    latitude: float

    class Config:
        orm_mode = True
