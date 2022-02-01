from math import pi

r = float(input())
s1 = round(r**2 * pi, 6)
s2  = round(2 * r**2, 6)

print(s1, s2, sep='\n')