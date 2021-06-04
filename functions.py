import numpy
from numpy import  sqrt, sum
# Fonksiyon Blokları
def prod( it ):
    p= 1
    for n in it:
        p *= n
    return p

def Ufun(x,a,k,m):
    y=k*((x-a)**m)*(x>a)+k*((-x-a)**m)*(x<(-a));
    return y

#zakharov
def zakharov( x ):
    x = numpy.asarray_chkfinite(x)
    n = len(x)
    j = numpy.arange( 1., n+1 )
    s2 = sum( j * x ) / 2
    return sum( x**2 ) + s2**2 + s2**4

#powell
def powell( x ):
    x = numpy.asarray_chkfinite(x)
    n = len(x)
    n4 = ((n + 3) // 4) * 4
    if n < n4:
        x = numpy.append( x, numpy.zeros( n4 - n ))
    x = x.reshape(( 4, -1 ))  # 4 rows: x[4i-3] [4i-2] [4i-1] [4i]
    f = numpy.empty_like( x )
    f[0] = x[0] + 10 * x[1]
    f[1] = numpy.sqrt(5) * (x[2] - x[3])
    f[2] = (x[1] - 2 * x[2]) **2
    f[3] = sqrt(10) * (x[0] - x[3]) **2
    return sum( f**2 )

#sum2
def sum2(x):
    x = numpy.asarray_chkfinite(x)
    n = len(x)
    j = numpy.arange(1., n + 1)
    return sum(j * x ** 2)

def getFunctionDetails(a):
    # [name, lb, ub, dim]
    param = {  0: ["zakharov",-100,100,30],
               1 : ["powell",-10,10,30],
               2 : ["sum2",-100,100,30],
            }
    return param.get(a, "nothing")
