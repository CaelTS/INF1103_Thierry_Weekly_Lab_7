class Inventory:
    """Manages a collection of Product objects."""

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        """Add a product. Returns False if the ID is already taken."""
        if self.search_product(product.product_id) is not None:
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id):
        """Return the matching Product, or None if there isn't one."""
        for product in self.__products:
            if product.matches_id(product_id):
                return product
        return None

    def display_all(self):
        print("\nCurrent Inventory")
        print("\n-----------------------------------------------------")
        if len(self.__products) == 0:
            print("No products in Inventory!")
        for product in self.__products:
            print(product)
        print("-----------------------------------------------------")

    def get_products(self):
        """Hand back a copy of the list so outside code can't mess with ours."""
        return list(self.__products)
