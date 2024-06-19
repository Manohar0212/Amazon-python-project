# Using anonymous function
prime_factors = lambda n: [i for i in range(2, n+1) if n%i == 0 and all(i % j != 0 for j in range(2, int(i**0.5)+1))]
n = 315
factors = []
while n > 1:
	for factor in prime_factors(n):
		factors.append(factor)
		n //= factor
print(factors)


