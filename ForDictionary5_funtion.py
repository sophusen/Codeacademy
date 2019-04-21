#Define a function compute_bill that takes one argument food as input.

#In the function, create a variable total with an initial value of zero.

#For each item in the food list, add the price of that item to total.

#Finally, return the total.

#Ignore whether or not the item you're billing for is in stock.Note that your function should work for

#shopping_list = ["banana", "orange", "apple"]

#stock = {
#  "banana": 6,
#  "apple": 0,
#  "orange": 32,
#  "pear": 15
#}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Write your code below!
def compute_bill(food):
  total = 0
  for item in food:
    total = total + prices[item]
  return total
#(Make the following changes to your compute_bill function:

#While you loop through each item of food, only add the price of the item to total if the item's stock count is greater than zero.

#if the item is in stock and after you add the price to the total, subtract one from the item's stock count.)

def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
    	total = total + prices[item]
    	stock[item] = stock[item] -1
  return total
print compute_bill(shopping_list)
