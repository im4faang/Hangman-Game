import random, os
from art import stages,logo
from words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display  = []
for _ in chosen_word:
  display.append("_")

print(logo)

should_end = False
lives = 6
while not should_end:
  guess = input("Guess a letter: ").lower()
  os.system("clear")
  if guess in display:
    print(f"You've already guessed {guess}")

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    print(f"You guessed {guess},that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      should_end = True
      print(f"The word you were looking for is {chosen_word}. You lose.")  

  print(f"{' '.join(display)}")    

  if "_" not in display:
    should_end = True
    print("You win!")

  print(stages[lives])
