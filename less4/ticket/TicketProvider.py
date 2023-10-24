from datetime import datetime

from Ticket import Ticket
from TicketRepository import TicketRepository


class TicketProvider:

    def __init__(self, ticket_repository: TicketRepository) -> None:
        self.__ticket_repository = ticket_repository

    def update_ticket_status(self, id: int) -> bool:
        if self.__ticket_repository.update_ticket(id):
            return True
        return False

    def get_ticket(self, date_time: datetime) -> list[Ticket]:
        return self.__ticket_repository.read_ticket(date_time)