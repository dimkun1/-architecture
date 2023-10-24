from abc import ABC, abstractmethod

from Carrier import Carrier


class ICarrierRepo(ABC):

    @abstractmethod
    def create_carrier(self, carrier: Carrier):
        ...

    @abstractmethod
    def read_carrier(self, carrier_id: int) -> Carrier:
        ...

    @abstractmethod
    def update_carrier(self, carrier_id: int, **kwargs) -> None:
        ...

    @abstractmethod
    def delete_carrier(self, carrier_id: int) -> bool:
        ...