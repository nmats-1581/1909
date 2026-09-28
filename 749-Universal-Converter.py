def SSDec(n, a):
    if a=='0':
        return 0
    sa = a[a.find('-')+1:]
    s = 0
    for i in range(len(sa)-1, -1, -1):
        a1 = sa[len(sa)-i-1]
        if '0'<=a1<='9':
            s += int(a1)*(n**i)
        else:
            s += (ord(a1)-65+10)*(n**i)
    if a.find('-')==0:
        s *= -1
    return s
def SSK(k, a):
    if a==0:
        return 0
    s = ''
    A1 = abs(a)
    while A1:
        x = A1%k
        if 0<=x<=9:
            s += str(x)
        else:
            s += chr(x+(65-10))
        A1 //= k
    s = s[::-1].lstrip('0')
    if a<0:
        s = '-' + s
    return s
n = int(input())
a = input()
k = int(input())
print(SSK(k, SSDec(n, a)))