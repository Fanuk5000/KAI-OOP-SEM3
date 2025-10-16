# Internet-послуга:
# вибір тарифної моделі, надання доступу
# користувачеві, поповнення рахунку,
# підсумки трафіку, користування Internet
# та ін.

from typing import Callable, Protocol
class TrafficEventArgs:
    def __init__(self, traffic_amount: float, limit: float, used: float):
        self.traffic_amount = traffic_amount
        self.limit = limit
        self.used = used

class Event:
    def __init__(self):
        self._handlers: list[Callable] = []

    def __iadd__(self, handler: Callable):
        self._handlers.append(handler)
        print("Event created.", self._handlers)
        return self

    def __isub__(self, handler: Callable):
        self._handlers.remove(handler)
        return self

    def __call__(self, sender, args):
        for handler in self._handlers:
            handler(sender, args)

class IInternetService(Protocol):
    traffic_exceeded: Event
    traffic_limit: float
    __balance: float
    __is_connected: bool

    def use_internet(self, used_traffic: float) -> None: ...
    def __give_access(self) -> None: ...
    def on_traffic_exceeded(self, args: TrafficEventArgs) -> None: ...

class InternetService:
    def __init__(self, traffic_limit: float):
        self.traffic_limit = traffic_limit
        self.traffic_exceeded = Event()  # event instance
        self.__balance = 0.0
        self.__is_connected = False
    
    def use_internet(self, used_traffic: float):
        if used_traffic > self.traffic_limit:
            exceeded = used_traffic - self.traffic_limit
            args = TrafficEventArgs(exceeded, self.traffic_limit, used_traffic)
            self.on_traffic_exceeded(args)
        else:
            print(f"Traffic within limit: {used_traffic} / {self.traffic_limit} GB")

    def __give_access(self) -> None:
        if self.__balance > 0:
            self.__is_connected = True
            print("Access granted.")
        else:
            self.__is_connected = False
            print("Access denied. Please top up your balance.")
   
    def on_traffic_exceeded(self, args: TrafficEventArgs):
        # call all event handlers
        self.traffic_exceeded(self, args)