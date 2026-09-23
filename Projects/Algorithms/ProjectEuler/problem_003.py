"""
The prime factors of 13195  are 5,7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
n = 13195

for i in range(1, 13196):
	n%i
	if n%i==0:
		print(i)



