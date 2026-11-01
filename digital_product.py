from product import Product


class DigitalProduct(Product):
    """A product that is delivered as a download. It does not need shipping,
    so it does not implement CanBeShipped."""

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        if download_size <= 0:
            raise ValueError("Download size must be more than 0 MB.")
        self.__download_size = float(download_size)

    @property
    def download_size(self):
        return self.__download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size:.2f} MB")

    def get_fulfilment_info(self):
        return "Digital product: delivered to the customer as a download, no shipping needed."

    def __str__(self):
        return f"{super().__str__()} | Download Size: {self.__download_size:.2f} MB"
