def gcd(a,b):
    return a if b==0 else gcd(b,a%b)

##最大公约数，欧几里得算法

print(gcd(44,11))