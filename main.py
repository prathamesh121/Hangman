import random

word_list = ["anushka", "payal", "amina", "ruchita"]
chosen_word = random.choice(word_list)
# print(f'psst,')

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

    print(display)

    if "_" not in display:

        end = True
        print("You win")
      
