index = ["1","2","3","4","5","6","7","8","9"]

def displayBoard():
    for i in range(len(index)):
        if i%3==0:
            print("\n-------------------\n¦",end="")
        print(" ",index[i]," ",end="¦")
    print("\n-------------------")
