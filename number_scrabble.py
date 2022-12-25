def turnChecker(pnum, pname1, pname2):
    if pnum % 2 == 0:
        return pname1
    else:
        return pname2


def winCheck(pnums):
    winner = [0]
    for i in range(0, len(pnums) - 2):
        for j in range(i+1, len(pnums) - 1):
            for k in range(j+1, len(pnums)):
                if pnums[i] + pnums[j] + pnums[k] == 15:
                    winner = [pnums, pnums[i], pnums[j], pnums[k]]
    return winner


terminate = ""
while terminate != "x":
    print("\n\n     NUMBER SCRABBLE     \n\n")
    # player names input
    pname1 = input("Enter Player 1 Name: ")
    if pname1 == "":
        pname1 = "Player 1"
    pname2 = input("Enter Player 2 Name: ")
    if pname2 == "":
        pname2 = "Player 2"
    pnum = 0
    p1nums = []
    p2nums = []
    nums = list(range(1, 10))

    while nums != []:
        print(nums)
        pname = turnChecker(pnum, pname1, pname2)

        # Turns input
        while True:
            try:
                turn = int(input(pname + " turn: "))
                if turn in nums:
                    break
                else:
                    print("The input should be a number from ", nums, ": ")
            except ValueError:
                print("The input should be a number from ", nums, ": ")

        if pname == pname1:
            p1nums.append(turn)
        elif pname == pname2:
            p2nums.append(turn)

        # Win Check
        if len(p1nums) > 2:
            winner = winCheck(p1nums)
            if p1nums == winner[0]:
                print("\n\n", pname1, "Win!\n", winner[1], "+",
                      winner[2], "+", winner[3], "= 15\n\n")
                break
        if len(p2nums) > 2:
            winner = winCheck(p2nums)
            if p2nums == winner[0]:
                print("\n\n", pname2, "Win!\n", winner[1], "+",
                      winner[2], "+", winner[3], "= 15\n\n")
                break
        nums.remove(turn)
        pnum += 1
    print("\nDRAW !\n")
    terminate = input("press any key to start again, or x to exit. ")
