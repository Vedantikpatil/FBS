###WAP to calculate selling price of book based on cost price and discount. 

cp=int(input("Enter cost price:"))
discount=int(input("Enter discount:"))
discount_amount=(cp*discount)/100
selling_price=cp-discount_amount
print("selling price = ", selling_price)