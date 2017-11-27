def createsent():
    s = []
    n = int(input("How many words long is your sentence going to be ?  "))
    m = n
    while n > 0:
        s.append(input("Input word by word the sentence  "))
        n = n - 1
    ss = s[n]
    n = n + 1
    while n < m:
        ss = ss + " " + s[n]
        n = n + 1
    print(ss)
    return ss
        
def invert(sen):
    if sen == "":
        return sen  
    else:
        return(invert(sen[1:]) + sen[0])
        
def display(let):
    a = ""
    a = let + a
    print(a)
        
       
    
  
display(invert(createsent()))
