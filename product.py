from abc import ABC, abstractmethod


class Product(ABC):
    """Abstract base class for every product.

    Holds what all products share and manages that state. A product has to be
    a specific kind (physical or digital), so Product itself can't be created.
    """

    def __init__(self, product_id, name, price, stock):
        if str(product_id).strip() == "":
            raise ValueError("Product ID cannot be empty.")
        if str(name).strip() == "":
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if stock < 0:
            raise ValueError("Stock cannot be negative.")

        self.__product_id = str(product_id).strip()
        self.__name = str(name).strip()
        self.__price = float(price)
        self.__stock = int(stock)

    # Read-only access, so outside code can look but not change things directly
    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    def update_stock(self, quantity):
        """Set the stock to a new quantity. The product decides what is allowed."""
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self.__stock = int(quantity)

    def matches_id(self, product_id):
        """True if this product has the given ID (not case sensitive)."""
        return self.__product_id.lower() == str(product_id).strip().lower()

    def display_information(self):
        """Print the details every product has. Subclasses add their own on top."""
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    @abstractmethod
    def get_fulfilment_info(self):
        """Return a message describing how this product gets to the customer."""
        pass

    def __str__(self):
        # One line summary, used when listing every product
        return (f"ID: {self.__product_id} | Name: {self.__name} | "
                f"Price: ${self.__price:.2f} | Stock: {self.__stock}")
