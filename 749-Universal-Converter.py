def SSDec(n, a):
    if a=='0':
        return 0
    a1 = a[a.find('-')+1:]
    s = 0
    p = 1
    for i in range(len(a1)-1, -1, -1):
        if '0'<=a1[i]<='9':
            s += (ord(a1[i])-48)*p
        else:
            s += (ord(a1[i])-55)*p
        p *= n
    if a[0]=='-':
        s *= -1
    return s
def SSK(k, a):
    if a==0:
        return 0
    s = ''
    a1 = abs(a)
    while a1:
        x = a1%k
        if 0<=x<=9:
            s = chr(x+48) + s
        else:
            s = chr(x+55) + s
        a1 //= k
    if a<0:
        s = '-' + s
    return s
n = int(input())
a = input()
k = int(input())
print(SSK(k, SSDec(n, a)))