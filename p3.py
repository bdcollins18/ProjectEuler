import math

def sieve():
	primes = list()
	test_prime = 2
	is_prime = True #Flag is True until proven false by checking against list of primes
	while True:
		for known_prime in primes:
			if test_prime % known_prime == 0:
				is_prime = False
				break
		if is_prime:
			primes.append(test_prime)
			yield test_prime
		test_prime += 1
		is_prime = True

primes = sieve()
n = 600851475143
largest = 0
for prime in primes:
	if n % prime == 0:
		largest = prime
	if prime > math.sqrt(n):
		break

print(largest)