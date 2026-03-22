products = ["Chips" ,"Jelly" ,"Choclate" ,"Juice" ,"Bread"]
tax_price = []
for product in products:
    price = int(input(f"Price of {product} : "))
    tax = round(price*1.1,2)
    tax_price.append(tax)

total = sum(tax_price)
expensive = max(tax_price)

print("Prices with Tax are :" , tax_price)
print(f"Total is : {total:.2f}")
print(f"Most Expensive was : {expensive:.2f}")