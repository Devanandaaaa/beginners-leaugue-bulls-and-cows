import random

def generate_number():
    """Generate a 4-digit number from digits 1-9 without duplication."""
    digits = random.sample(range(1, 10), 4)
    return ''.join(map(str, digits))

def is_valid_guess(guess):
    """Check if guess is 4 unique digits from 1-9."""
    return (guess.isdigit() and
            len(guess) == 4 and
            all(d in '123456789' for d in guess) and
            len(set(guess)) == 4)

def score_guess(secret, guess):
    """Return bulls and cows count."""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows

def play_game():
    secret_number = generate_number()
    

    print("Welcome to Bulls and Cows!")
    print("Guess the 4-digit number (digits 1-9, no duplicates).")

    while True:
        guess = input("Enter your guess: ").strip()

        if not is_valid_guess(guess):
            print("Invalid guess! Use 4 unique digits from 1-9.")
            continue

        if guess == secret_number:
            print("🎉 You guessed it right! The number was", secret_number)
            break

        bulls, cows = score_guess(secret_number, guess)
        print(f"{bulls} Bulls, {cows} Cows")

if __name__ == "__main__":
    play_game()
