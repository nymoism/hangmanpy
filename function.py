import random 
from words import words


def select_word(li):
    return random.choice(li)

def validWord():
    return [w for w in words if len(w) > 5]

def display_words(word,guess):
    return ' '.join([c if c in guess else '_' for c in word ])

# def used_letters(letter):
#     return [i for i in word if letter not in word ]
    
def play_hang():
    words = validWord()
    word = select_word(words)
    guesses = set()
    attempts = 6
    used_letters = []
    while attempts > 0:
        print(display_words(word,guesses))
        letter = input("Enter A Letter:")
        letter.lower()
        guesses.add(letter)

        if len(letter) > 1:
            print("Invalid. ONe Letter At A Time")

        if letter not in word:
            attempts -= 1
            used_letters.append(letter)
            print(used_letters)
            print(f"{letter} is not a Letter")

        if set(word) <= guesses:
            print("You Win!")
            print(word)
            return
    print("Out of tries")
    print(f"the word was {word}")

            
        

