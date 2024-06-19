# Python3 Program to
# find sum of square
# of first n natural
# numbers

# Return the sum of
# square of first n
# natural numbers


def squaresum(n):
	return (n * (n + 1) * (2 * n + 1)) // 6


# Driven Program
n = 4
print(squaresum(n))

# ___________________________________________________


n = 4
sum = 0
for i in range(1, n+1):
	sum += i**2

print("The sum of squares of first", n, "natural numbers is", sum)

