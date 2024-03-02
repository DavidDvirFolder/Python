import random

display = []
word_list = ["apple"]
random_word = random.choice(word_list)
word_length = len(random_word)
print(random_word)
match_found = False

for i in range(word_length):
    display += "_"
print(display)

while "_" in display and word_length > 0:
    guess = input("Guess a letter: \n").lower()
    match_found = False  # Flag to check if a match is found
    for i in range(word_length):
        letter = random_word[i]
        if letter == guess:
            display[i] = letter
            match_found = True
        if not ("_" in display):
            print(f"Boom! , the word is:")
            break
    if not match_found:
        print(f"You have more {word_length} attempts!")
        word_length -= 1
    if word_length == 0:
        print("Game Over")
        break

    print("".join(display))
