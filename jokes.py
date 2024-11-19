
import random


def menu():
    print("Welcome to the joke program")
    print("Please enter a command")
    print("list - list all jokes")
    print("go - tell a random joke")





def main():
    jokes_list = [ ["What does a baby computer call his father?","Data"],
                   ["What do a tick and the Eiffel Tower have in common", "They're both Paris sites"]
                 ]
    menu()

    joke = random.choice(jokes_list)
    print(joke)





if __name__ == "__main__":
    main()
