food_price = input('food price: ')
print(food_price)
tip = 0.18 * int(food_price)
sales_tax = 0.07 * int(food_price)
print (int(tip))
print (int(sales_tax))
print ()
print ('Total cost: ' + str(int(food_price)+tip+sales_tax))