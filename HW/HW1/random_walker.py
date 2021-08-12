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
    print('Squared distance from origin:', distance ** 2)


def random_walker_sim(n, T):
    distances = []
    for exp in range(T):
        loc = [0, 0]
        directions = {'up': [0, 1], 'down': [0, -1], 'left': [-1, 0], 'right': [1, 0]}
        for step in range(n):
            direction = choice(list(directions.values()))
            loc = [sum(i) for i in zip(loc, direction)]
        x, y = loc
        sqr_distance = x ** 2 + y ** 2
        distances.append(sqr_distance)
    print('Mean squared distance for', n, 'steps and', T, 'experiments:', sum(distances) / len(distances))

    # Hypo - Squared distance is equal to the number of steps. COOL!!!!

##########################################################################
#                            End of your code                            #
##########################################################################


##########################################################################
#                           Start of your tests                          #
##########################################################################
#     Use as many test as you see fit. These tests will not be tested    #
##########################################################################
random_walker(40)
random_walker_sim(50, 1000)

##########################################################################
#                            End of your tests                           #
##########################################################################
