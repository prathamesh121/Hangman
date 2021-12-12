import random

word_list = ["anushka", "payal", "amina", "ruchita"]
chosen_word = random.choice(word_list)
# print(f'psst,')
lives = 6
display = []
word_len = len(chosen_word)
# //create a blank
for _ in range(word_len):
    display += "_"

print(display)

end = False

while not end:
    guess = input("Guess a letter \n").lower()

    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end = True
            print("you Lose")

    print(f"{' ' .join(display)}")

    if "_" not in display:

        end = True
        print("You win")

  #  print(stages[lives])   
