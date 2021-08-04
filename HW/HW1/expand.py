##########################################################################
#                           Start of your code                           #
##########################################################################
from string import digits


def expand(compressed_dna):
    dna = ''
    for i in range(len(compressed_dna)):
        n = 1
        if compressed_dna[i] in digits and compressed_dna[i - 1] not in digits:
            while (i + n < len(compressed_dna)) and (compressed_dna[i + n] in digits):
                n += 1
            dna += compressed_dna[i - 1] * int(compressed_dna[i:i + n])
    print(dna)


def test_expand():
    pass


##########################################################################
#                            End of your code                            #
##########################################################################


##########################################################################
#                           Start of your tests                          #
##########################################################################
#     Use as many test as you see fit. These tests will not be tested    #
##########################################################################

expand('G2T11C4A5T1')


##########################################################################
#                            End of your tests                           #
##########################################################################
