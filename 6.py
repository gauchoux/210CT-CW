def crealist():
    L = []
    n = int(input("How long is your list going to be ?  "))
    while n > 0:
        L.append(int(input("Input number one by one  ")))
        n = n - 1
    return(L)

def targ():
    targ = int(input("Enter target number  "))
    return(targ)

def search(array, target):
    if len(array) == 0:
        print("Not found")
    elif array[0] == target:
        print("Found")
        return True
    else:
        return(search(array[1:],target))

search(crealist(),targ())
