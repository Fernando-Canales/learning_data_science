"""
Problem 0 from Project Euler
Fernando
17th of August, 2026
"""

odd_squares = []
for i in range(1, 107001):
	i = i**2
	if i%2 != 0:
		odd_squares.append(i)


print("El resultado es: ", sum(odd_squares), "¡Qué numerote!")
