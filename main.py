import random


def hide_word(word, guessed_letters):
    hidden = ""
    for letter in word:
        if letter in guessed_letters:
            hidden += letter
        else:
            hidden += "*"
    return hidden


def main():
    word_list = ["apple", "banana", "cherry", "grape", "orange", "strawberry"]
    word = random.choice(word_list)
    attempts = int(input("Введіть кількість спроб: "))
    guessed_letters = []

    while attempts > 0:
        print("\nЗагадане слово:", hide_word(word, guessed_letters))
        guess = input("Введіть літеру або слово: ").lower()

        if guess == word:
            print("Вітаю, ви вгадали слово!")
            break
        elif guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("Ви вже вводили цю літеру.")
            elif guess in word:
                guessed_letters.append(guess)
                if hide_word(word, guessed_letters) == word:
                    print("Вітаю, ви вгадали слово!", word)
                    break
            else:
                attempts -= 1
                print("Такої літери немає. Залишилось спроб:", attempts)
        else:
            print("Невірний ввід. Будь ласка, введіть літеру або слово.")

        if attempts == 0:
            print("Ви програли. Загадане слово:", word)


if __name__ == "__main__":
    main()
