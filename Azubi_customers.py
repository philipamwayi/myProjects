#Azubi store has products that customers love. Below are the products, prices and the number of customers that purchased products last week.

# The owner wants you to do some calculations on the data with these criteria's:

#     -calculate the total price average for all products

#     -create a new price list that reduces the old prices by $ 5

#     -calculate the total revenue generated from the products

#     -calculate the average daily revenue generated from the products

#     -based on the new prices, which products are less than $ 30 

# Below is the data you are to use for the problem :

# products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

# prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

# last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

new_prices=[]
new_list=[]
low_prices={}

average=sum(prices)/len(prices)
print('The total price average for all products is : ' + str(average))
for price in prices:
    new_price=price-5
    new_prices.append(new_price)

print('The new Price list after reduction is :' + str(new_prices))

for a in range(0, len(prices)):
    new_list.append(prices[a]*last_week[a])

b=(sum(new_list))
print('The total revenue generated from the sale is : ' + str(b))
print('The average daily revenue generated from the products is : ' + str(b/len(new_list)))

low_prices=dict(zip(products, new_prices))
print(low_prices)
#print(low_prices)

for key, value in low_prices.items():
    if (low_prices.values() <= 20):
        print(key, value)