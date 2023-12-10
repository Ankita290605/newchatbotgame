import random

class ChatbotGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.guesses = 0
        self.max_guesses = 10

    def greet(self):
        return "Welcome to the Guess the Number game! I'm thinking of a number between 1 and 100."

    def get_hint(self, guess):
        self.guesses += 1
        if guess < self.secret_number:
            return "Too low! Try a higher number."
        elif guess > self.secret_number:
            return "Too high! Try a lower number."
        else:
            return f"Congratulations! You guessed the correct number {self.secret_number} in {self.guesses} guesses."

    def play(self):
        response = self.greet()
        print(response)

        while True:
            try:
                guess = int(input("Enter your guess: "))
                hint = self.get_hint(guess)
                print(hint)

                if guess == self.secret_number or self.guesses == self.max_guesses:
                    break

            except ValueError:
                print("Please enter a valid number.")

if __name__ == "__main__":
    game = ChatbotGame()
    game.play()