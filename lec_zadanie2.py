import numpy 
import lec_zadanie1 as fc

h = 100
a = numpy.radians(45)
b = numpy.radians(35)

skobki = 1 - numpy.tan(b) * numpy.tan(a)
chislitel = fc.g * h * numpy.tan(b)
znaminatel = 2 * numpy.cos(a) **2

v = numpy.sqrt(chislitel / znaminatel * skobki)

print(v)


# T = 200
# c = 300
# kk = fc.k

# N = 2 / numpy.sqrt (numpy.pi) * numpy.sqrt(fc.h) * (kk * T) ** 3/2  * fc.e * c/kk*T * c ** T/2

# print(N)