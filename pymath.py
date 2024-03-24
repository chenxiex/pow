def mypow(a,b,m=0):
    result=1
    while b>0 :
        if (b&1==1):
            result=result*a
            if m!=0:
                result%=m
        a*=a
        if m!=0:
            a%=m
        b>>=1
    return result

def exgcd(a,b):
    if b==0:
        return (1,0,a)
    else:
        x,y,g=exgcd(b,a%b)
        return (y,x-(a//b)*y,g)

def mminverse(a,m):
    x,y,g=exgcd(a,m)
    if g!=1:
        return None
    else:
        return (x+m)%m

def montgomery_mul(x, y, mod, inv):
    n = x * y
    m = (n * inv) & ((1 << mod.bit_length()) - 1)
    r = (n + m * mod) >> mod.bit_length()
    if r >= mod:
        r -= mod
    return r

def montgomery_pow(x, power, mod):
    inv = mminverse(-mod, 1 << mod.bit_length())
    x=x*(1<<mod.bit_length())%mod
    result=(1<<mod.bit_length())%mod
    while power:
        if power & 1:
            result = montgomery_mul(result, x, mod, inv)
        x = montgomery_mul(x, x, mod, inv)
        power >>= 1
    return montgomery_mul(result, 1, mod, inv)