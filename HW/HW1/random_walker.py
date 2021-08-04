##########################################################################
#                           Start of your code                           #
##########################################################################
from random import choice


def random_walker(n):
    loc = [0, 0]
    directions = {'up': [0, 1], 'down': [0, -1], 'left': [-1, 0], 'right': [1, 0]}
    print(tuple(loc))
    for step in range(n):
        direction = choice(list(directions.values()))
        loc = [sum(i) for i in zip(loc, direction)]
        print(tuple(loc))
    x, y = loc
    distance = (x ** 2 + y ** 2) ** 0.5
    print('Squared distance from origin:', distance ** 0.5)


def random_walker_sim(n, T):
    distances = []
    for exp in range(T):
        loc = [0, 0]
        directions = {'up': [0, 1], 'down': [0, -1], 'left': [-1, 0], 'right': [1, 0]}
        for step in range(n):
            direction = choice(list(directions.values()))
            loc = [sum(i) for i in zip(loc, direction)]
        x, y = loc
        distance = ((x ** 2 + y ** 2) ** 0.5) ** 0.5
        distances.append(distance)
    print('Mean squared distance for', n, 'steps and', T, 'experiments:', sum(distances) / len(distances))


##########################################################################
#                            End of your code                            #
##########################################################################


##########################################################################
#                           Start of your tests                          #
##########################################################################
#     Use as many test as you see fit. These tests will not be tested    #
##########################################################################
random_walker(10)
random_walker_sim(100, 1000)

##########################################################################
#                            End of your tests                           #
##########################################################################
