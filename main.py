index = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def displayBoard():
    for i in range(len(index)):
        if i % 3 == 0:
            print("\n-------------------\n¦", end="")
        print(" ", index[i], " ", end="¦")
    print("\n-------------------")


def plotter(position, player):
    if player == 1:
        index[position - 1] = "X"
    elif player == 2:
        index[position - 1] = "O"
    else:
        print("This is an error from the plotter function, the problem is the player name is not 1 nor 2.")


def check_winner():
    win_checker_for_X_S = ((index[0] == "X" and index[1] == "X") and index[2] == "X") or (
            (index[3] == "X" and index[4] == "X") and index[5] == "X") or (
                                  (index[6] == "X" and index[7] == "X") and index[8] == "X")
    win_checker_for_X_U = ((index[0] == "X" and index[3] == "X") and index[6] == "X") or (
            (index[1] == "X" and index[4] == "X") and index[7] == "X") or (
                                  (index[2] == "X" and index[5] == "X") and index[8] == "X")
    win_checker_for_X_D = ((index[0] == "X" and index[4] == "X") and index[8] == "X") or (
            (index[2] == "X" and index[4] == "X") and index[6] == "X") or (
                                  (index[2] == "X" and index[5] == "X") and index[8] == "X")

    win_checker_for_O_S = ((index[0] == "O" and index[1] == "O") and index[2] == "O") or (
            (index[3] == "O" and index[4] == "O") and index[5] == "O") or (
                                  (index[6] == "O" and index[7] == "O") and index[8] == "O")
    win_checker_for_O_U = ((index[0] == "O" and index[3] == "O") and index[6] == "O") or (
            (index[1] == "O" and index[4] == "O") and index[7] == "O") or (
                                  (index[2] == "O" and index[5] == "O") and index[8] == "O")
    win_checker_for_O_D = ((index[0] == "O" and index[4] == "O") and index[8] == "O") or (
            (index[2] == "O" and index[4] == "O") and index[6] == "O") or (
                                  (index[2] == "O" and index[5] == "O") and index[8] == "O")

    if (win_checker_for_X_D or win_checker_for_X_S) or win_checker_for_X_U:
        return "The Winner Is X"
    elif (win_checker_for_O_D or win_checker_for_O_S) or win_checker_for_O_U:
        return "The Winner Is O"
    else:
        return "No One Yet"


def board_full():
    if sorted(list(set(index))) == ["O","X"]:
        return True
    else:
        return False

def main():
    intro = "Welcome To Tic Tac Toe\nPlayer 1 is X and Player 2 is O"
    print(intro)
    while True:

        again = input("Do you want to play? Yes Or No : ")

        if again == "Yes":
            pass
        else:
            break

        while check_winner() == "No One Yet":
            displayBoard()
            print("Player 1, it is your go!")
            plotter(int(input("Enter Position : ")), 1)
            check_winner()
            if check_winner() == "The Winner Is X":
                displayBoard()
                print(check_winner())
                break
            elif board_full():
                displayBoard()
                print("Draw")
                break

            displayBoard()
            print("Player 2, it is your go!")
            plotter(int(input("Enter Position : ")), 2)
            if check_winner() == "The Winner Is O":
                displayBoard()
                print(check_winner())
                break
            elif board_full():
                displayBoard()
                print("Draw")
                break


if __name__ == "__main__":
    main()
