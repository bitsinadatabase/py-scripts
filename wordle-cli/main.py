import random

from colorama import init, Fore, Style
import nltk
from nltk.corpus import words as dictionary


# Initializations
init()
nltk.download("words")


def print_guess(guess, answer):
    print(Style.BRIGHT, end = "")
    for idx, letter in enumerate(guess):
        if letter == answer[idx]:
            print(Fore.GREEN + letter + Fore.RESET, end = " ")
        elif letter in answer:
            print(Fore.YELLOW + letter + Fore.RESET, end = " ")
        else:
            print(Fore.WHITE + letter + Fore.RESET, end = " ")
    print(Style.RESET_ALL + "")


def print_keys(done_letters, answer):
    print("| " + Style.BRIGHT, end = "")
    for letter in "abcdefghijklmnopqrstuwxyz":
        if letter in done_letters and letter in answer:
            print(Fore.GREEN + letter + Fore.RESET, end = " ")
        elif letter in done_letters and not (letter in answer):
            print(Fore.RED + letter + Fore.RESET, end = " ")
        else:
            print(Fore.WHITE + letter + Fore.RESET, end = " ")
    print(Style.RESET_ALL + " |")


if __name__ == "__main__":

    length = int(input("Enter length of the words for difficulty - "))
    words = [word.lower() for word in dictionary.words() if len(word) == length]
    random.shuffle(words)
    
    quit = False
    played = 0
    won = 0
    streak = 0

    while not quit:
        print("=" * 10 + " NEW WORDLE " + "=" * 10)
        answer = words[played]

        played += 1
        done = False
        count = 0
        guess = "_" * length
        done_letters = []
        erase_keys = False
        
        print_guess(guess, answer)
        while not done:
            
            guess = input(f"Guess No. {count + 1} - ")
            if erase_keys:
                print ("\033[A" + " " * 100 + "\033[A")
            print ("\033[A" + " " * 100 + "\033[A")
            if len(guess) != length:
                erase_keys = False
                continue
            done_letters += list(guess)
            count += 1

            print_guess(guess, answer)
            print_keys(done_letters, answer)
            erase_keys = True

            if guess == answer:
                won += 1
                streak += 1
                done = True
                print(f"Played - {played}, Won - {won}, Streak - {streak}")
            elif count == length:
                streak = 0
                done = True
                print(f"Answer - {answer}")
                print(f"Played - {played}, Won - {won}, Streak - {streak}")

        quit = input("Press q to quit, anything else to continue.\n") == "q"

    print(f"Played - {played}, Won - {won}, Streak - {streak}")
