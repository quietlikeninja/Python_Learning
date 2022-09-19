import random

def input_validation(inputMessage, validationType):
  while True:
    if validationType == "Question":
        userInput = input(inputMessage)
        if userInput:
            return userInput
            break
        else:
            print("Question can't be blank!")
            continue
    elif (validationType == "Yes or No"):
        yesnoOptions = ["y", "n", "yes", "no"]
        yesno = input(inputMessage)
        if yesno.lower() in yesnoOptions:
            return yesno.lower()
            break
        else:
            print("Invalid option try again. Please enter Y or N.\n")
            continue 

def main():
    name = input("What's your name? ")
    question = input_validation("Ask a yes/no question: ", "Question")
    answer = ""
    random_number = random.randint(1,9)

    if random_number == 1:
        answer = "Yes - definitely."
    elif random_number == 2:
        answer = "It is decidedly so."
    elif random_number == 3:
        answer = "Without a doubt."
    elif random_number == 4:
        answer = "Reply hazy. try again."
    elif random_number == 5:
        answer = "Ask again later."
    elif random_number == 6:
        answer = "Better not tell you now."
    elif random_number == 7:
        answer = "My sources say no."
    elif random_number == 8:
        answer = "Outlook not so good."
    elif random_number == 9:
        answer = "Very doubtful."
    else:
        answer = "Error"

    if name != "":
        print(f"{name} asks: {question}")
    else:
        print(f"Question: {question}")

    print(f"Magic 8-Ball's answer: {answer}")

if __name__ == "__main__":
    while True:
        main()

        if (input_validation("Do you have another question? Y/N " ,"Yes or No") in ["y", "yes"]):
            continue
        else:
            print("Thanks for playing, see you next time")
            break