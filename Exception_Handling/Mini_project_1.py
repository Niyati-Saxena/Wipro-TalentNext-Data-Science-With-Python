# Mini project - 1
# Write a Python program that reads purchase details from a text file.
# Each line contains either:
#   - an item name followed by its price (e.g., "Soap 40"),
#   - "Free" as the price indicating a free item (e.g., "Pen Free"),
#   - or the word "Discount" followed by a discount amount (e.g., "Discount 15").
# The program should:
#   1. Count total items purchased
#   2. Count number of free items
#   3. Calculate total amount before discount
#   4. Extract the discount amount
#   5. Compute final amount after applying the discount
# Handle all exceptions such as file not found, invalid price formats, and malformed lines.

try:
    filename = input("Enter the file name: ")
    total_items = 0
    free_items = 0
    amount_to_pay = 0
    discount = 0

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) == 2:
                name, value = parts
                if value.lower() == "free":
                    free_items += 1
                    total_items += 1
                elif name.lower() == "discount":
                    try:
                        discount = float(value)
                    except ValueError:
                        print(f"Invalid discount format: {value}")
                else:
                    try:
                        amount_to_pay += float(value)
                        total_items += 1
                    except ValueError:
                        print(f"Invalid price for item '{name}': {value}")
            else:
                print(f"Skipping malformed line: {line}")

    final_amount = amount_to_pay - discount

    print("No of items purchased:", total_items)
    print("No of free items:", free_items)
    print("Amount to pay:", int(amount_to_pay))
    print("Discount given:", int(discount))
    print("Final amount paid:", int(final_amount))

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
except Exception as e:
    print("An error occurred:", str(e))
