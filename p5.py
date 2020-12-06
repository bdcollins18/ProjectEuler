def sieve(n):
	primes = list()
	test_prime = 2
	is_prime = True #Flag is True until proven false by checking against list of primes
	while test_prime <= n:
		for known_prime in primes:
			if test_prime % known_prime == 0:
				is_prime = False
				break
		if is_prime:
			primes.append(test_prime)
			yield test_prime
		test_prime += 1
		is_prime = True

primes = list(sieve(20))
prime_factors = dict()
for prime in primes:
	prime_factors[prime] = 0
for i in range(1,21):
	while i > 1:
		for prime in primes:
			n = 0
			while i % prime == 0:
				i //= prime
				n += 1
			if n > prime_factors[prime]:
				prime_factors[prime] = n

n = 1
for factor in prime_factors:
	while prime_factors[factor] > 0:
		n *= factor
		prime_factors[factor] -= 1

print(n)
