
food = ['hamburger', 'sushi', 'pizza']
price = [30.5, 40, 60.99]
calories = [500, 400, 470]

menu = {food[i]: {price[i]: calories[i]} for i in range(len(food))}
print(menu)
