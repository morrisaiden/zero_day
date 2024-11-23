def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    :param price: Original price of the item (float or int)
    :param discount_percent: Discount percentage to apply (float or int)
    :return: Final price after applying the discount if discount >= 20%, otherwise the original price
    """
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        return price - discount
    return price


# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Output the result
    if final_price < original_price:
        print(f"The final price after applying a discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
