# Module to calculate the hypotenuse of a right angle triangle
# Will have two functions, one to get the squares of the opp and the adj
# One to calculate the square root of those added together
# a**2 + b**2 = c **2

# Function to get the squares of opp and adj

#Input/args: opp and ajd (a and b)
#Outputs/returns: a**2 and b**2

def square(opp, adj):
    opp_sq = opp**2
    adj_sq = adj**2
    return opp_sq, adj_sq

print(square(3,4))

# Function to calc the sqrt of those added
#Input/args: a**2 and b**2
#Output/returns: c or the hypotenuse

def hypotenuse(opp_sq, adj_sq):
    sum_o_a = opp_sq + adj_sq
    sqrt = (sum_o_a)**0.5
    return sqrt

def pythag(opp, adj):
    opp_sq, adj_sq = square(opp, adj)
    h = hypotenuse(opp_sq, adj_sq)
    return h