import math
#prime generator from http://stackoverflow.com/questions/567222/simple-prime-generator-in-python
def gen_primes(end):
    D = {}
    q = 2
    while q <= end:
        if q not in D:
            yield q
            D[q*q]=[q]
        else:
            for p in D[q]:
                D.setdefault(p+q, []).append(p)
            del D[q]
        q+=1    
target = 600851475143
out = 0
end = int(math.sqrt(target))
primes = [i for i in gen_primes(end)]
for i in primes:
    if target%i==0:
        out = i
print out
