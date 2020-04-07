def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a,a)

def lcm(a,b):
    return int((a*b)/gcd(a,b))


a=25
b=15
print(lcm(a,b))