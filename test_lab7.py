"""Quick checks for Lab 7 (section 7). Run with: python test_lab7.py"""
from can_be_shipped import CanBeShipped
from digital_product import DigitalProduct
from inventory import Inventory
from physical_product import PhysicalProduct
from product import Product


def check(description, condition):
    print(f"[{'PASS' if condition else 'FAIL'}] {description}")


guitar = PhysicalProduct("T001", "Guitar", 450.0, 5, 3.5)
heavy = PhysicalProduct("T002", "Amp", 800.0, 2, 12.0)
game = DigitalProduct("T003", "Puzzle Game", 14.99, 999, 320.0)

print("--- Physical product ---")
guitar.display_information()
print("\n--- Digital product ---")
game.display_information()
print()

check("Physical product stores its weight", guitar.weight == 3.5)
check("Digital product stores its download size", game.download_size == 320.0)
check("Physical get_fulfilment_info() works", "shipped" in guitar.get_fulfilment_info())
check("Digital get_fulfilment_info() works", "download" in game.get_fulfilment_info())

try:
    Product("X001", "Generic", 1.0, 1)
    check("Product cannot be created directly", False)
except TypeError as error:
    print(f"        (Python said: {error})")
    check("Product cannot be created directly", True)

check("Physical product can calculate shipping", guitar.calculate_shipping_cost() == 5.00 + 2.50 * 3.5)
check("Heavier product costs more to ship", heavy.calculate_shipping_cost() > guitar.calculate_shipping_cost())
check("Physical product is a CanBeShipped", isinstance(guitar, CanBeShipped))
check("Digital product is not a CanBeShipped", not isinstance(game, CanBeShipped))
check("Digital product has no shipping method", not hasattr(game, "calculate_shipping_cost"))

inventory = Inventory()
check("Inventory accepts physical product", inventory.add_product(guitar))
check("Inventory accepts digital product", inventory.add_product(game))
check("Inventory rejects duplicate ID", not inventory.add_product(PhysicalProduct("t001", "Dup", 1, 1, 1)))
check("Inventory search finds product", inventory.search_product("t003") is game)
game.update_stock(10)
check("Stock update works", game.stock == 10)
