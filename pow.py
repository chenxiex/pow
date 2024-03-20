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

if __name__=='__main__':
    a,b,m=map(int,input().split())
    print(mypow(a,b,m))