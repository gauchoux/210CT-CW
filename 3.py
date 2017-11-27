def createpol():
    print("Create the two polynomials")
    global Deg1
    global Deg2
    global P1
    global P2
    Deg1 = int(input("Degree of your 1st polynomial:  "))
    Deg2 = int(input("Degree of your 2nd polynomial:  "))
    P1 = []
    P2 = []

    a= Deg1 + 1
    print("You need ", a, " coefficients for your first polynomial")
    print(", enter them one by one, tapping enter between each number, from the left of the polynomial to the right")
    while a > 0:
        b = int(input())
        P1.append(b)
        a = a - 1
    
    a= Deg2 + 1
    print("You need ", a, " coefficients for your second polynomial")
    print(", enter them one by one, tapping enter between each number, from the left of the polynomial to the right")
    while a > 0:
        b = int(input())
        P2.append(b)
        a = a - 1


def addpol():
    createpol()  
    global Deg1
    global Deg2
    global P1
    global P2
    NewP = []
    if Deg1 > Deg2:
        Deg3 = Deg1
        while (Deg2 + 1) > 0:
            NewP.append((P1[Deg1]+P2[Deg2]))
            Deg1 = Deg1 - 1
            Deg2 = Deg2 - 1
        while (Deg1 + 1) > 0:
            NewP.append((P1[Deg1]))
            Deg1 = Deg1 - 1
        NewP = NewP[::-1]
    if Deg2 > Deg1:
        Deg3 = Deg2
        while (Deg1 + 1) > 0:
            NewP.append((P1[Deg1]+P2[Deg2]))
            Deg1 = Deg1 - 1
            Deg2 = Deg2 - 1
        while (Deg2 + 1) > 0:
            NewP.append((P2[Deg2]))
            Deg2 = Deg2 - 1
        NewP = NewP[::-1]
    if Deg1 == Deg2:
        Deg3 = Deg1
        while (Deg1 + 1) > 0:
            NewP.append((P1[Deg1]+P2[Deg2]))
            Deg1 = Deg1 - 1
            Deg2 = Deg2 - 1
    print("New Polynome obtained in list form", NewP)
    print("With a degree of", Deg3)
    again()
    
    
def multpol():
    createpol()  
    global Res
    Deg3 = Deg1 + Deg2
    Res = [0] * (Deg1 + Deg2 + 1)
    for i in range(Deg1 + 1):
        for j in range(Deg2 + 1):
            Res[i+j] = Res[i+j] + P1[i]*P2[j]
    print("New Polynome obtained in list form", Res)
    print("With a degree of", Deg3)
    again()
    
    
def derivpol():
    createpol()
    global Deg1
    global Deg2
    global P1
    global P2
    DerP1 = []
    DerP2 = []
    DerDeg1 = Deg1 - 1
    DerDeg2 = Deg2 - 1
    P1 = P1[::-1]
    while Deg1 > 0:
        DerP1.append(Deg1 * P1[Deg1])
        Deg1 = Deg1 - 1
    print("The derivative form of the first polynomial in a list", DerP1)
    print("And it's degree", DerDeg1)
    P2 = P2[::-1]
    while Deg2 > 0:
        DerP2.append(Deg2 * P2[Deg2])
        Deg2 = Deg2 - 1
    print("The derivative form of the second polynomial in a list", DerP2)
    print("And it's degree", DerDeg2)
    again()


def main():
    a = int(input("Do you want to multiply, enter 1, add, enter 2, or derive, enter 3, two polynomials ?  ") )
    if a == 1:
        multpol()
    if a == 2:
        addpol()
    if a == 3:
        derivpol()
    else:
        print("Enter 1, 2 or 3 !!")
        main()
        
def again():
    a = int(input("Do you want to start again, enter 1, or stop, enter 2 ?  ") )
    if a == 1:
        main()
    if a == 2:
        print("End")
        return False
    else:
        print("Enter 1 or 2 !!")
        again()

main()
