def createlist():
    L = []
    a = int(input("How long do you wish your list to be ?  "))
    while a > 0:
        b = int(input("Enter number you wish to add  "))
        L.append(b)
        a = a - 1
    return L

def ispalin(l):
    k = l[::-1]
    if k == l:
        print("This array is a palindrome")
    else:
        print("This array is not a palindrome")
        
ispalin(createlist())
