from User import User
from IUserRepo import IUserRepo


class UserRepository(IUserRepo):

    __user_repository: list[User] = []

    def __init__(self) -> None:
        pass

    @property
    def repository(self) -> list[User]:
        return self.__user_repository

    def create_user(self, user: User):
        self.__User_repository.append(user)

    def read_user(self, user_id: int) -> User:
        for user in self.__user_repository:
            if user.id == user_id:
                return User

    def update_user(self, user_id: int, **kwargs) -> bool:
        for user in self.__user_repository:
            if user.id == user_id:
                ...
            return True
        return False

    def delete_user(self, user_id: int) -> bool:
        for user in self.__user_repository:
            if user.id == user_id:
                self.__user_repository.remove(user)
                return True
        return False