index = ["1","2","3","4","5","6","7","8","9"]

def displayBoard():
    for i in range(len(index)):
        if i%3==0:
            print("\n-------------------\n¦",end="")
        print(" ",index[i]," ",end="¦")
    print("\n-------------------")

def plotter(position,player):
    if player == 1:
        index[position] = "X"
    elif player == 2:
        index[position] = "O"
    else:
        print("This is an error from the plotter function, the problem is the player name is not 1 nor 2.")