a = input("Input 3 digit number:  ")
n1 = int(a[0])
n2 = int(a[1])
n3 = int(a[2])
if int(a) == n1**3 + n2**3 + n3**3:
    print("True")
else:
    print("False")
