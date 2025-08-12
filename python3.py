def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, applies the discount.
    Otherwise, returns the original price.
    """
    # Check if discount is 20% or more
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Subtract discount from original price
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

# Prompt the user for input
try:
    # Ask user to enter the original price
    original_price = float(input("Enter the original price of the item: "))
    # Ask user to enter the discount percentage
    discount_percentage = float(input("Enter the discount percentage: "))

    # Call the function to calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Display the final price, formatted to two decimal places
    print(f"The final price after discount is: {final_price:.2f}")

except ValueError:
    # Handle invalid input (non-numeric values)
    print("Please enter valid numeric values for price and discount.")
