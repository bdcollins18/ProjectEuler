import math

def isPalindrome(n):
	order_of_magnitude = math.floor(math.log10(n))
	if order_of_magnitude == 0:
		return True
	else:
		forward = n
		backward = 0
		next_place = int(math.pow(10, order_of_magnitude))
		for i in range(order_of_magnitude + 1):
			backward += next_place * (n % 10)
			next_place //= 10
			n //= 10
		return forward == backward


x_min = 1
x_max = 999
y_min = 1
y_max = 999

palindrome_max = 0
for x in range(x_min, x_max + 1):
	for y in range(y_min, y_max + 1):
		product = x * y
		if product > palindrome_max and isPalindrome(product):
			palindrome_max = product

print(palindrome_max)