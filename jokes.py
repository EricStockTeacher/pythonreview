
import random








def main():
    jokes_list = [ ["What does a baby computer call his father?","Data"],
                   ["What do a tick and the Eiffel Tower have in common", "They're both Paris sites"]
                 ]

    joke = random.choice(jokes_list)
    print(joke)





if __name__ == "__main__":
    main()
