from base import Location
from typing import Tuple


class LocationDummy(Location):
    """
    ダミーの位置情報(東京スカイツリー)
    """

    def address_to_latitude_and_longitude(self, address: str) -> Tuple[float, float]:
        return 35.7101, 139.8086

    def __init__(self, address="東京都墨田区押上1-1-2"):
        super().__init__(address)


def main():
    location = LocationDummy()
    attributes = [f"{key}: {value}" for key, value in location.__dict__.items()]
    print(", ".join(attributes))


main()
