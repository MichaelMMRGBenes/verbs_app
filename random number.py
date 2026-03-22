import random
def secret_number():
    row = []
    for i in range(1,20):
        row.append(i)

    random.shuffle(row)

    n = row[0]
    return n
def main():
    n = secret_number()
    while True:
        guessed = int(input("Can you guess the random number for 1-20? "))
        if guessed == n:
            print("yes! Thats it")
            print("Do you want to play again?")
            again = input("(Y)es or (N)o! ")
            if again.capitalize() == "Y":
                print("Ok! Lets play again!")
                n = secret_number()
                continue
            else:
                print("Ok! Enough for today!")
                break

        elif guessed > n:
            print("No, the secret number is smaller")
        else:
            print("No, the secret number is bigger")

main()