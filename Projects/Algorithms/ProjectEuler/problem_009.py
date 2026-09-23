"""
A Pythagorean triplet is a set of three natural numbers, a<b<c , for which,

For example,3^2+4^2=5^2      .

There exists exactly one Pythagorean triplet for which a+b+c=1000 .
Find the product abc.
"""

import numpy as np

for a in range(1,1001):
	for b in range(1,1001):
		c = 1000 - a - b
		if a**2 + b**2 == c**2:
			print(a*b*c)

