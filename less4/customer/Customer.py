from datetime import datetime

from ICustomer import ICustomer
from ticket.Ticket import Ticket
from ticket.TicketProvider import TicketProvider
from cash.CashProvider import CashProvider


class Customer(ICustomer):

    __selected_tickets: list[Ticket] = []

    def __init__(self, ticket_provider: TicketProvider, cash_provider: CashProvider) -> None:
        self.__ticket_provider = ticket_provider
        self.__cash_provider = cash_provider

    @property
    def selected_tickets(self) -> list[Ticket]:
        return self.__selected_tickets

    def search_ticket(self, id: int, date_time: datetime) -> list[Ticket]:
        return [ticket for ticket in self.ticket_provider.get_ticket() if ticket.id == id and ticket.date_time == date_time]

    def buy_ticket(self, ticket: Ticket) -> bool:
        self.__selected_tickets.append(ticket)
        return self.cash_provider.buy_ticket()