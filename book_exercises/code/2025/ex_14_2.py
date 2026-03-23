from datetime import datetime, timedelta


class Ticket():
    """The Ticket class is defined for general transport vehicles"""

    def __init__(self, customer="your_name", price=20):
        self.customer = customer
        self.price = price

    # Methods of the class


class Metro(Ticket):
    """"Metro tickets"""

    def __init__(self, customer="", price=0):
        super().__init__(customer=customer, price=price)
        self.valid_from_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.valid_until_time = (datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    ticket = Metro(customer="Ron Dicaprio", price=54)
    print(f"Ticket valid from: {ticket.valid_from_time}")
    print(f"Ticket valid until: {ticket.valid_until_time}")
