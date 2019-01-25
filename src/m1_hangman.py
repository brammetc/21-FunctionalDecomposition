"""
Hangman.

Authors: Tanner Brammeier and Haley Braker.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######
import random


def main():
    print('started')
    word, integer2 = stage2()
    char = stage3(word, integer2)
    stage4(word, integer2)


def stage1():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
        r = random.randrange(0, len(words))
        item = words[r]
        print(item)
    return item


def stage2():
    print("I will choose a random secret word from a dictionary. You set the MINIMUM length of that world.")
    string = input("What MINIMUM length do you want for the secret word?")
    integer = int(string)

    string2 = input("How many unsuccessful choices do you want to allow yourself?")
    integer2 = int(string2)

    while True:
        word = stage1()
        if len(stage1()) >= integer:
            word2 = len(word)
            print("Here is what you currently know about the secret word:")
            print(word)
            for k in range(word2):
                print('-', end='')
            break
    return word, integer2


def stage3(word, integer2):
    string = input("What letter do you want to try?")
    char = str(string)
    for k in range(0, len(word)):
        if char == word[k]:
            print("yay")
            print('You still have', integer2, 'tries left!')
            return char, integer2
    print('No!!!!')
    integer2 = integer2 - 1
    print('You have', integer2, 'tries left!')
    return integer2


def stage4(word, integer2):
    while True:
        if integer2 > 0:
            # for k in range(integer2-1):
            stage3(word, integer2)
            return word, integer2
        else:
            print("You are out of tries!")
main()
