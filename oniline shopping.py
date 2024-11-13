price_shirt = 30
price_pants = 40
price_tshirts = 60
price_shorts = 30
qty_shirt = 5
qty_pants = 5
qty_tshirts = 5
qty_shorts = 5
total_shirt = price_shirt * qty_shirt
total_pants = price_pants * qty_pants
total_tshirts = price_tshirts * qty_tshirts
total_shorts = price_shorts * qty_shorts
total_cart = total_shirt + total_shorts + total_tshirts + total_pants
print("shopping cart")
print(f"shirts {qty_shirt} ${total_shirt}")
print(f"pants {qty_pants} ${total_pants}")
print(f"tshirts {qty_tshirts} ${total_tshirts}")
print(f"shorts {qty_shorts} ${total_shorts}")
print(f"Total Cost: ${total_cart}")
submit = input("Type 'submit' to complete your purchase: ")
if submit.lower() == "submit":
    print("Purchase completed! Thank you for shopping with us.")
else:
    print("Purchase not completed.")