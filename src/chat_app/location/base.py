from abc import ABC, abstractmethod
from typing import Tuple


class Location(ABC):
    address: str
    latitude: float
    longitude: float

    def __init__(self, address: str):
        self.address = address
        self.latitude, self.longitude = self.address_to_latitude_and_longitude(self.address)

    @abstractmethod
    def address_to_latitude_and_longitude(self, address: str) -> Tuple[float, float]:
        pass
