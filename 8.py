def main():
    print("\n")
    print("     |----------------------------------------|") 
    print("     |  Think of a number between 1 and 2000  |")
    print("     |     Tap enter when you are ready       |")
    print("     |----------------------------------------| \n")
    input()
    guess(biglist())
    

def biglist():
    L=[]
    for i in range(1,2001):
        L.append(i)
    return L

def guess(arr):
    
    if len(arr) == 1:
        print("The number you're thinking of is " + arr)

    a = input(" Is the number " + str(arr[int(len(arr)/2)-1]) + " ? Yes or No ? ")
    if a == "Yes" or a == "yes":
            print("\n I win, I guessed you were thinking of the number " + str(arr[int(len(arr)/2)-1]))
            
    elif a == "No" or a == "no":
            b = input("\n Is it higher or lower than " + str(arr[int(len(arr)/2)-1]) + " ? ")
            if b == "Higher" or b == "higher":
                for i in range(arr[0], arr[int(len(arr)/2)]):
                    arr.remove(i)
                guess(arr)
            elif b == "Lower" or b == "lower":
                for i in range(arr[int(len(arr)/2)], (arr[int(len(arr)-1)] + 1)):
                    arr.remove(i)
                guess(arr)
            else:
                print("Enter a valid answer")
                guess(arr)
    else:
        print("Enter a valid answer \n")
        guess(arr)
                    
                
main()
