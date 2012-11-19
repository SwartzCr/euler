def is_palindrome(num):
    number = str(num)
    for i in range(len(number)/2):
        if number[i] != number[-(i+1)]:
            return False
    return True

out = 0

for i in range(999,100,-1):
    j = i
    print i
    while j>100:
        cur = j*i
        if is_palindrome(cur):
            print cur
            if cur>out:
                out = cur
            break
        print j
        j-=1
print out
