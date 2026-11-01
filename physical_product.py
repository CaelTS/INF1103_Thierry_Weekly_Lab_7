from can_be_shipped import CanBeShipped
from product import Product

# Simple shipping rule: a flat base fee plus a charge for every kilogram
BASE_SHIPPING_FEE = 5.00
COST_PER_KG = 2.50


class PhysicalProduct(Product, CanBeShipped):
    """A product that is stored in a warehouse and shipped to the customer.

    Inherits from Product (is-a) and signs the CanBeShipped contract.
    """

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        if weight <= 0:
            raise ValueError("Weight must be more than 0 kg.")
        self.__weight = float(weight)

    @property
    def weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self):
        return "Physical product: needs to be packed and shipped to the customer."

    def calculate_shipping_cost(self):
        return BASE_SHIPPING_FEE + COST_PER_KG * self.__weight

    def __str__(self):
        return f"{super().__str__()} | Weight: {self.__weight:.2f} kg"
