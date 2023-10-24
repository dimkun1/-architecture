from cash.BankAccount import BankAccount

class User:

    def __init__(self, id: int, user_name: str, hash_password: int, bank_account: BankAccount) -> None:
        self.__id = id
        self.__user_name = user_name
        self.__hash_password = hash_password
        self.__bank_account = bank_account

    @property
    def id(self) -> int:
        return self.__id

    def set_id(self, id: int) -> None:
        self.__id = id

    @property
    def user_name(self) -> str:
        return self.__user_name

    def set_user_name(self, user_name: str) -> None:
        self.__user_name = user_name

    @property
    def hash_password(self) -> int:
        return self.__hash_password

    def set_hash_password(self, hash_password: int) -> None:
        self.__hash_password = hash_password

    @property
    def bank_account(self) -> BankAccount:
        return self.__bank_account

    def set_bank_account(self, bank_account: BankAccount) -> None:
        self.__bank_account = bank_account