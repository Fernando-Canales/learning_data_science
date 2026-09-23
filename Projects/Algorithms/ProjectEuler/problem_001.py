"""
Problem 1
If we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .

Find the sum of all the multiples of  or  below .

Solved by Fernandito
August 17th, 2026
"""

multiples_of_3_or_5 = []

for i in range(1, 1000):
	if i%3==0 or i%5==0:
		multiples_of_3_or_5.append(i)

print("El resutlado es: ", sum(multiples_of_3_or_5), "¡Qué numerote!")
