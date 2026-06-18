import random

words = ("apple", "orange", "banana", "coconut", "cherry")

# dictionary of wrong_guesses -> lines of ASCII art for the hangman figure
hangman_art = {
    0: ("  +---+",
        "  |   |",
        "      |",
        "      |",
        "      |",
        "      |",
        "========="),
    1: ("  +---+",
        "  |   |",
        "  O   |",
        "      |",
        "      |",
        "      |",
        "========="),
    2: ("  +---+",
        "  |   |",
        "  O   |",
        "  |   |",
        "      |",
        "      |",
        "========="),
    3: ("  +---+",
        "  |   |",
        "  O   |",
        " /|   |",
        "      |",
        "      |",
        "========="),
    4: ("  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        "      |",
        "      |",
        "========="),
    5: ("  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        " /    |",
        "      |",
        "========="),
    6: ("  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        " / \\  |",
        "      |",
        "=========")
}


def display_man(wrong_guesses):
    """Print the hangman figure matching the current number of wrong guesses."""
    for line in hangman_art[wrong_guesses]:
        print(line)


def display_hint(hint):
    """Print the word as guessed-so-far, with un-guessed letters shown as underscores."""
    print(" ".join(hint))


def display_answer(answer):
    """Reveal the correct answer."""
    print(f"The word was: {answer}")


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    max_wrong_guesses = 6
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'.\n")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = letter
        else:
            wrong_guesses += 1
            print(f"'{guess}' is not in the word.\n")

        if "_" not in hint:
            display_man(wrong_guesses)
            display_hint(hint)
            print(f"You won! The word was '{answer}'.")
            is_running = False
        elif wrong_guesses >= max_wrong_guesses:
            display_man(wrong_guesses)
            print("You lost!")
            display_answer(answer)
            is_running = False


if __name__ == "__main__":
    main()