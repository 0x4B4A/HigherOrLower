import random as ran
num = 0
win = False
playnum = 0
attempt = 0

print ("""Choose your gamemode!
1 - Easy (1-50, 10 attempts)
2 - Medium (1-100, 15 attempts)
3 - Hard (1-500, 20 attempts)
4 - Super Hard (1-1000, 25 attempts)""")

while num == 0:
    mode = input("> ")
    if mode == "1":
        num = ran.randint(1, 50)
        attempt = 20
    elif mode == "2":
        num = ran.randint(1, 100)
        attempt = 15
    elif mode == "3":
        num = ran.randint(1, 500)
        attempt = 10
    elif mode == "4":
        num = ran.randint(1, 1000)
        attempt = 10
    else:
        print("error, redo...")

print("Number Chosen; Input any number and I will tell you if my number is higher or lower!")

while win == False:
    if attempt == 0:
        print("You Lose :( Ran out of attempts!)")

    else:
        print("You have " + str(attempt) + " attempt('s) left.")
        playnum = input ("> ")
        playnum = int(playnum)
        if playnum == num:
            print("Correct, You Win!")
            win = True
        elif playnum < num:
            print("My Number Is Higher!")
            attempt=attempt-1
        elif playnum > num:
            print("My Number Is Lower!")
            attempt=attempt-1
