##########################################################################
#                           Start of your code                           #
##########################################################################
def approx_pi(n):
    pi = 0
    for i in range(n):
        pi += 4 * (((-1) ** i) / (2*i + 1))

    return pi


##########################################################################
#                            End of your code                            #
##########################################################################


##########################################################################
#                           Start of your tests                          #
##########################################################################
#     Use as many test as you see fit. These tests will not be tested    #
##########################################################################
print(approx_pi(10))  # should return 3.0418396189294032
print(approx_pi(1000))  # should return 3.140592653839794
print(approx_pi(100000))  # should return 3.1415826535897198
print(approx_pi(1000000))
print(approx_pi(0))
##########################################################################
#                            End of your tests                           #
##########################################################################
