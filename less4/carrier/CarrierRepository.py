from Carrier import Carrier
from ICarrierRepo import ICarrierRepo


class CarrierRepository(ICarrierRepo):

    __Carrier_repository: list[Carrier] = []

    def __init__(self) -> None:
        pass

    @property
    def repository(self) -> list[Carrier]:
        return self.__carrier_repository

    def create_carrier(self, carrier: Carrier):
        self.__carrier_repository.append(carrier)

    def read_carrier(self, carrier_id: int) -> Carrier:
        for carrier in self.__carrier_repository:
            if carrier.id == carrier_id:
                return carrier

    def update_carrier(self, carrier_id: int, **kwargs) -> bool:
        for carrier in self.__carrier_repository:
            if carrier.id == carrier_id:
                ...
                return True
        return False

    def delete_carrier(self, carrier_id: int) -> bool:
        for carrier in self.__carrier_repository:
            if carrier.id == carrier_id:
                self.__carrier_repository.remove(carrier)
                return True
        return False