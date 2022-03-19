while True:
    import random
    randnum=random.randint(1,100)
    guesses=0
    userguess= None
    print("1.Easy(1), 2.Medium(2), 3.Hard(3")
    diff=int(input("Choose a difficulty:"))

    if (diff==1):
        randnum=random.randint(1,100)
        guesses=0
        userguess= None
        while(userguess != randnum):
            userguess=int(input("Guess a random number: "))
            guesses += 1
            if (userguess==randnum):
                print("Correct! You win!")
            else:
                if (userguess>randnum):
                    print("Too High!Guess a little lower in next guess!")
                elif(userguess<randnum):
                    print("Too low!Guess a litle higher in next guess!")
            

        print(f"You guessed the number in {guesses} guess(es)")
        with open("highscore.txt","r") as f:
            a=int(f.read())
        if guesses<a:
            print("You have just broken the high score!")
            with open("highscore.txt","w") as f:
                f.write(str(guesses))

    if (diff==2):
        randnum=random.randint(1,1000)
        guesses=0
        userguess= None
        while(userguess != randnum):
            userguess=int(input("Guess a random number: "))
            guesses += 1
            if (userguess==randnum):
                print("Correct! You win!")
            else:
                if (userguess>randnum):
                    print("Too High!Guess a little lower in next guess!")
                elif(userguess<randnum):
                    print("Too low!Guess a litle higher in next guess!")
            

        print(f"You guessed the number in {guesses} guess(es)")
        with open("mehighscore.txt","r") as f:
            a=int(f.read())
        if guesses<a:
            print("You have just broken the high score!")
            with open("mehighscore.txt","w") as f:
                f.write(str(guesses))

    if (diff==3):
        randnum=random.randint(1,10000)
        guesses=0
        userguess= None
        while(userguess != randnum):
            userguess=int(input("Guess a random number: "))
            guesses += 1
            if (userguess==randnum):
                print("Correct! You win!")
            else:
                if (userguess>randnum):
                    print("Too High!Guess a little lower in next guess!")
                elif(userguess<randnum):
                    print("Too low!Guess a litle higher in next guess!")
            

        print(f"You guessed the number in {guesses} guess(es)")
        with open("hahighscore.txt","r") as f:
            a=int(f.read())
        if guesses<a:
            print("You have just broken the high score!")
            with open("hahighscore.txt","w") as f:
                f.write(str(guesses))

    if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
        break
