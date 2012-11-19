import math
#prime generator from http://stackoverflow.com/questions/567222/simple-prime-generator-in-python
def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q*q]=[q]
        else:
            for p in D[q]:
                D.setdefault(p+q, []).append(p)
            del D[q]
        q+=1    
for n,i in enumerate(gen_primes()):
    if n+1==10001:
        print i
        break
