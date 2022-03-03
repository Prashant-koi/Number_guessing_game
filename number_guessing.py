import random
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

