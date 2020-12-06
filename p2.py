prev = 1
current = 2
sum = 0
while current < 4000000:
	if current % 2 == 0:
		sum += current
	next = prev + current
	prev = current
	current = next

print(sum)