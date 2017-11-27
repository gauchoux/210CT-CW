def crealist():
    L = []
    n = int(input("How long is your list going to be ?  "))
    while n > 0:
        L.append(int(input("Input number one by one  ")))
        n = n - 1
    return(L)

def insert(array):
    for i in range(1,len(array)):
        pos = i
        if (array[pos-1] > array[pos] and pos > 0) == True:
            print(array)
        while array[pos-1] > array[pos] and pos > 0:
            stock = array[pos-1]
            array[pos-1] = array[pos]
            array[pos] = stock
            pos = pos - 1
    print(array)       


def bubble(array):
    check = 0
    print(array)
    while check != 9:
        check = 0
        for i in range(1,len(array)):
            pos = i
            if array[pos-1] > array[pos]:
                stock = array[pos-1]
                array[pos-1] = array[pos]
                array[pos] = stock
            else:
                check = check + 1
        print(array)
                

def selection(array):
    print(array)
    for i in range(1,len(array)):
        pos = i
        minpos = i - 1
        for j in range(pos,len(array)):
            if array[minpos] > array[j]:
                stock = array[minpos]
                array[minpos] = array[j]
                array[j] = stock
        print(array)

def main():
    L = [2,7,9,4,1,5,3,6,0,8]
    a = int(input("Do you want to insert sort, type 1, bubble sort, type 2, \n or selection sort, type 3 ?  "))
    b = int(input("Do you want to use the CW array ([2,7,9,4,1,5,3,6,0,8]), type 1, \n or generate one yourself, type 2 ?  "))
    if a == 1:
        if b == 1:
            insert(L)
        elif b == 2:
            insert(crealist())
        else:
            print("You entered wrong numbers, try again")
            main()
    elif a == 2:
        if b == 1:
            bubble(L)
        elif b == 2:
            bubble(crealist())
        else:
            print("You entered wrong numbers, try again")
            main()
    elif a == 3:
        if b == 1:
            selection(L)
        elif b == 2:
            selection(crealist())
        else:
            print("You entered wrong numbers, try again")
            main()
    else:
        print("You entered wrong numbers, try again")
        main()

main()
