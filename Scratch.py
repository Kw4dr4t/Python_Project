m = int(input('podaj 1 wartosc: '))
n = int(input('podaj 2 wartosc: '))
c = m * n
while m != n:
    if m > n:
        m -= n
    else:
        n -= m
    nww = c / n
    print(nww)
# NWW (najmniejsza wspolna wielokrotnosc) dla zbioru liczb
# www.algorytm.org

from functools import reduce


# oblicza NWD (najwiekszy wspolny dzielnik) dla dwoch liczb
def gcd(a, b):
    while b != 0:
        b, a = a % b, b
    return a


# oblicza NWW (najmniejsza wspolna wielokrotnosc) dla dwoch liczb
def lcm(a, b):
    """
	lcm(3, 8) => 24
	"""
    return abs(a * b / gcd(a, b))


# oblicza NWW (najmniejsza wspolna wielokrotnosc) dla listy liczb
def lcm_list(l):
    """
		lcm_list([3, 4, 5, 6]) => 60
	"""
    return reduce(lcm, l, 1)


print(gcd(12, 4))
print(lcm(6, 8))
print((lcm_list([2, 3, 4, 5, 6, 7])))
