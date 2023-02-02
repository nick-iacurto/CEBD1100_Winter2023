customer_type = input("Customer type - R/W: ")
ct = customer_type.lower()
invoice_total = float(input("Invoice total: "))
discount_percentage = 0.0

if customer_type == "R":
    if invoice_total >= 100 and invoice_total < 250:
        discount_percentage = 0.1
    elif invoice_total >= 250:
        discount_percentage = 0.2
elif customer_type == "W":
    if invoice_total < 500:
        discount_percentage = 0.4
    elif invoice_total >= 500:
        discount_percentage = 0.5
else:
    print("Code is not valid.")

print(f"Discount determined is {discount_percentage}")
