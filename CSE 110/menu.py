child_meal = input("How much is a kid's meal? ")
adult_meal = input("And how much is an adult meal? ")
kids = input("How many kids are there? ")
adults = input("And how many adults are present? ")
drink_price = float(input("How much are drinks?"))
drink_number =int(input("How many drinks do you guys want?"))
tax = input("Now I know this isn't very clasy, but how much is sales tax? ")
child_meal_price = float(child_meal)
adult_meal_price = float(adult_meal)
number_kids = int(kids)
number_adults = int(adults)
sales_tax= float(tax)
print("")
subtotal = round(child_meal_price * number_kids + adult_meal_price * number_adults + drink_price * drink_number,2)
print(f"Subtotal: ${subtotal}")
tax_actual = round(subtotal * sales_tax,2)
print(f"Sales Tax: ${tax_actual}")
total = round(subtotal + tax_actual,2)
print(f"Total: ${total}")
print("")
payment = float(input("What is the payment amount? "))
change = round(payment - total,2)
print(f"Chnage comes out to: ${change}")
print("Have a great day!")