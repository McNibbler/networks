#Calculate probability of more than N users being online
from math import factorial

testUsersSimultaneous = 10
testUsers = 35
testProbPerUser = 0.1

#nCr helper function for prob function
def nCr(n,r):
	return ((factorial(n))//(factorial(r) * factorial( n - r )))

#uses binomial distribution to find the probability of at
#least n users transmitting and subtracts to find the
#probability that more than n users are transmitting
def prob(users, usersSimultaneous, probPerUser):
    binom = 0
    for i in range(0,usersSimultaneous + 1):
        binom += nCr(users, i)*(probPerUser**i) \
        *((1 - probPerUser)**(users - i))
    return (1 - binom)

print("For", testUsers, "users, the probability of\nmore than", testUsersSimultaneous, "users being online at\nonce is", prob(testUsers, testUsersSimultaneous, testProbPerUser))