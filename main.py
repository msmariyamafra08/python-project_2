word = "python"
guessed = set()
lives = 6

while lives > 0:
    shown = "".join(c if c in guessed else "_" for c in word)
    print(f"\nWord: {shown}   Lives: {lives}")
    if "_" not in shown:
        print("You got it!")
        break
    letter = input("Guess a letter: ").strip().lower()[:1]
    if letter in word:
        guessed.add(letter)
        print("Yes!")
    else:
        lives -= 1
        print("Nope.")
else:
    print("Out of lives. The word was", word)
