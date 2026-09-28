def DigitCounter(s):
    c = 0
    for i in s:
        if i.isdigit():
            c+=1
    return c 
s = input()
print(DigitCounter(s))