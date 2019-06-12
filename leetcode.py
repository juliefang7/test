# Reverse the digits in an integar
# INPUT x is the integar we want to reverse

# OUTPUT solution is the reversed number
def reverse( x):
    y = str(x)
    solution = ''
    for i in reversed(y):
        solution += i
    print (solution)
    return solution


reverse (234)
