import random
from tkinter import *

import pygame

FONT_NAME = "Courier"
NUM_OF_TRY = 0
RANDOM_GUESS = 0
BIG_NUM = 0
pygame.mixer.init()


# --------------------------------------brain--------------------------------------------------------#
def sound(value):
    if value == 1:
        pygame.mixer.init()
        test = pygame.mixer.Sound("sound/win.mp3")
        test.play()
    elif value == 0:
        test = pygame.mixer.Sound("sound/loss.mp3")
        test.play()
    elif value == 2:
        test = pygame.mixer.Sound("sound/close1.mp3")
        test.play()
    elif value == 3:
        test = pygame.mixer.Sound("sound/close2.mp3")
        test.play()
    elif value == -1:
        test = pygame.mixer.Sound("sound/far1.mp3")
        test.play()
    elif value == -2:
        test = pygame.mixer.Sound("sound/far2.mp3")
        test.play()
    elif value == 4:
        test = pygame.mixer.Sound("sound/start.mp3")
        test.play()


def start_ez():
    global NUM_OF_TRY
    NUM_OF_TRY = 3
    global RANDOM_GUESS
    global BIG_NUM
    BIG_NUM = 10
    randomGuess = random.randint(0, 10)
    RANDOM_GUESS = randomGuess

    right_wrong.config(text=f"the number is between 0 - {BIG_NUM}")
    sound(4)


def start_med():
    global NUM_OF_TRY
    NUM_OF_TRY = 5

    global BIG_NUM
    global RANDOM_GUESS
    randomGuess = random.randint(0, 100)
    RANDOM_GUESS = randomGuess
    BIG_NUM = 100
    right_wrong.config(text=f"the number is between 0 - {BIG_NUM}")
    sound(4)


def start_hard():
    global NUM_OF_TRY
    NUM_OF_TRY = 10
    global BIG_NUM
    global RANDOM_GUESS

    randomGuess = random.randint(0, 1000)
    BIG_NUM = 1000
    RANDOM_GUESS = randomGuess
    right_wrong.config(text=f"the number is between 0 - {BIG_NUM}")
    sound(4)


def check_win():
    global RANDOM_GUESS
    global BIG_NUM
    global NUM_OF_TRY

    top = BIG_NUM
    guess = int(guess_entry.get())
    random_guess = RANDOM_GUESS
    if NUM_OF_TRY >= 0:
        if random_guess == guess:
            right_wrong.config(text="YOU WON !")
            main_image.config(file="img/win.png")
            sound(1)
        elif abs(guess - random_guess) < top / 4:
            right_wrong.config(text="TOO CLOSE")
            main_image.config(file="img/close2.png")
            sound(2)
        elif abs(guess - random_guess) < top / 2:
            right_wrong.config(text="CLOSE")
            main_image.config(file="img/close1.png")
            sound(3)
        elif abs(guess - random_guess) < top * 0.75:
            right_wrong.config(text="FAR")
            main_image.config(file="img/far1.png")
            sound(-1)
        elif abs(guess - random_guess) > top * 0.75:
            right_wrong.config(text="TOO FAR")
            main_image.config(file="img/far2.png")
            sound(-2)
    else:
        main_image.config(file="img/loss.png")
        right_wrong.config(text="YOU LOST")
        sound(0)
    NUM_OF_TRY -= 1


# -----------------------------------UI------------------------------------------#
window = Tk()
window.minsize(width=470, height=650)
window.resizable(False, False)

head = Label(text="GUESS BY MEME", font=(FONT_NAME, 40, "bold"), padx=35, pady=0)
head.grid(column=0, row=0, columnspan=3)

difficulty = Label(text="DIFFICULTY", font=(FONT_NAME, 25, "bold"), pady=20)
difficulty.grid(column=0, row=2, columnspan=3)

ez_button = Button(text="EAZY", pady=10, width=25, command=start_ez)
ez_button.grid(column=0, row=3)

medium_button = Button(text="MEDIUM", pady=10, width=25, command=start_med)
medium_button.grid(column=1, row=3)

hard_button = Button(text="HARD", pady=10, width=25, command=start_hard)
hard_button.grid(column=2, row=3)

pad = Label(text=" ")
pad.grid(column=0, row=4, columnspan=3)

guess_entry = Entry(width=5)
guess_entry.grid(column=0, row=5, columnspan=3)

pad1 = Label(text=" ")
pad1.grid(column=0, row=6, columnspan=3)

guess_button = Button(text="GUESS", pady=20, width=20, command=check_win)
guess_button.grid(column=0, row=7, columnspan=3)

right_wrong = Label(text="right wrong", font=(FONT_NAME, 20, "bold"), pady=20)
right_wrong.grid(column=0, row=8, columnspan=3)

canvas = Canvas(height=250, width=250, highlightthickness=0)
main_image = PhotoImage(file="img/start.png")
canvas.create_image(125, 125, image=main_image)
canvas.grid(column=0, row=1, columnspan=3)

window.mainloop()
pygame.mixer.quit()
