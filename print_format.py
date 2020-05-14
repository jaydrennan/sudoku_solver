def print_nice(x):
    print("~~~~~~~~~~~~~~~~~~~~~")
    for count1, j in enumerate(x):
        for count, k in enumerate(j):
            print(str(k) + " ", end="")
            if count % 3 == 2 and count % 9 < 8:
                print("|", end="")
            elif count % 9 == 8:
                print()
        if count1 % 3 == 2 and count1 % 9 < 8:
            print("---------------------")
        elif count1 == 8:
            print("~~~~~~~~~~~~~~~~~~~~~")
