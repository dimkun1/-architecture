from abc import ABC, abstractmethod

from User import User


class IUserRepo(ABC):

    @abstractmethod
    def create_user(self, user: User):
        ...

    @abstractmethod
    def read_user(self, user_id: int) -> User:
        ...

    @abstractmethod
    def update_user(self, user_id: int, **kwargs) -> None:
        ...

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        ...