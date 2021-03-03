iword =input("Enetr a word")
length=len(iword)
if len(iword)>0 :
    #print(len(iword))
    #print(iword[0])
    #print(iword[-1])
    if (iword[0]==iword[-1]):
        print(iword ,"is a palindrome")
    else:
         print(iword ," is not a palindrome")
