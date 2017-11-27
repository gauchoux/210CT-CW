a = input("Input a word:  ")
b = input("Input an other word:  ")
d = len(a)
e = len(b)
f = 0
c = ""
if d < e:
    while d>0:
        c = c + a[f] + b[f]
        f = f + 1
        d = d - 1
        e = e - 1
    while e>0:
        c = c + b[f]
        f = f + 1
        e = e - 1      
    print(c)
if d > e:
    while e>0:
        c = c + a[f] + b[f]
        f = f + 1
        d = d - 1
        e = e - 1
    while d>0:
        c = c + a[f]
        f = f + 1
        d = d - 1      
    print(c)
if d == e:
    while d>0:
        c = c + a[f] + b[f]
        f = f + 1
        d = d - 1
        e = e - 1
    print(c)
        
