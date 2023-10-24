from datetime import datetime


class Ticket:

    def __init__(self, price: float, id: int, place: int, date_time: datetime = datetime.now(), is_valid: bool = False) -> None:
        self.__price = price
        self.__id = id
        self.__place = place
        self.__date_time = date_time
        self.__is_valid = is_valid

    @property
    def price(self) -> float:
        return self.__price

    def set_price(self, price: float) -> None:
        self.__price = price

    @property
    def id(self) -> int:
        return self.__id

    def set_id(self, id: int) -> None:
        self.__id = id

    @property
    def place(self) -> int:
        return self.__place

    def set_place(self, place: int) -> None:
        self.__place = place

    @property
    def date_time(self) -> datetime:
        return self.__date_time

    def set_date(self, date_time: datetime) -> None:
        self.__date_time = date_time

    @property
    def is_valid(self) -> bool:
        return self.__is_valid

    def set_valid(self, is_valid: bool) -> None:
        self.__is_valid = is_valid