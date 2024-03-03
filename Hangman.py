import random

display = []
word_list = ["Apple", "Banana", "Orange", "Mango", "Strawberry",
             "Pineapple", "Watermelon", "Avocado", "Cherry", "Blueberry",
             "Raspberry", "Grapefruit", "Kiwi", "Pomegranate", "Blackberry",
             "Peach", "Plum", "Apricot", "Lemon", "Lime",
             "Coconut", "Fig", "Papaya", "Nectarine", "Grape",
             "Cantaloupe", "Honeydew", "Cranberry", "Elderberry"]
random_word = random.choice(word_list).lower()
word_length = len(random_word)
print("Welcome to Hangman!")
end_of_game = False

for i in range(word_length):
    display += "_"
print(display)

while "_" in display and word_length > 0:
    guess = input("Guess a letter: \n").lower()
    end_of_game = False  # Flag to check if a match is found
    for i in range(word_length):
        letter = random_word[i]
        if letter == guess:
            display[i] = letter
            end_of_game = True
        if not ("_" in display):
            print(f"Congratulations! You guessed the word:")
            break
    if not end_of_game:
        print(f"Incorrect guess.")
        word_length -= 1
        print(f"Attempts left: {word_length}")
    if word_length == 0:
        print(f"Sorry, you've run out of attempts. The correct word was: {random_word}")
        break

    print("".join(display))
