from User import User
from UserRepository import UserRepository


class UserProvider:

    def __init__(self, user_repository: UserRepository) -> None:
        self.__user_repository = user_repository

    def get_user(self, id: int) -> User:
        return self.__user_repository.read_user(id)