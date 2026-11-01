from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    """Interface-style contract: anything that can be shipped must be able
    to work out what its shipping costs.

    No attributes and no shipping logic here, just the promise.
    """

    @abstractmethod
    def calculate_shipping_cost(self):
        """Return the shipping cost in dollars."""
        pass
