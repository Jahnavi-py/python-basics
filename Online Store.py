from random import choice

items = {"Tv" : 180, "Books" : 100, "Bounty" : 40}
def display_items():
    print("Welcome to online store!")
    print("Available items:")
    for item, price in items.items():
        print(f"{item}: ${price}")
def calculate_total(cart):
    total = 0
    for item in cart:
        total += items.get(item,0)
    return total
def apply_discount(total):
    if total > 200:
        print("Applying 5% discount for orders over $200")
        total -= total * 0.05
    return total
def shopping_cart():
    cart = []
    display_items()
    while True:
        item_choice = input("Enter the item you wanted to add to the cart or done to finish ")
        if item_choice.lower() == 'done':
            break
        elif item_choice.capitalize() in items:
            cart.append(item_choice.capitalize())
            print(f"{item_choice} added to cart.")
        else:
            print("Item not available. Please select from the list.")
    total_price = calculate_total(cart)
    print("\nItems in your cart:", cart)
    print(f"Total price before discount: ${total_price}")

    final_price = apply_discount(total_price)
    print(f"Final price after discount: ${final_price:.2f}")
shopping_cart()