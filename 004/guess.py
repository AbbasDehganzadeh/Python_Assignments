import random

guesses = list()  # list of guesses
quit_ = False  # Is showing the status of the program
MIN_, MAX_ = 1, 10
total = 0  # Total number of guesses

while not quit_:
    user_num = int(input("Enter a number in range {} and {} .".format(MIN_, MAX_)))
    sys_number = random.randint(MIN_, MAX_)  #! bots inclusive
    total += 1
    if user_num == sys_number:
        guesses.append(user_num)
        print("Correct: {}".format(user_num))
    else:
        print("Incorrect: {}\tthe correct[{}]".format(user_num, sys_number))
    yes = input("Press [q]uit to exit.")
    if yes[0].lower() == "q":
        quit_ = not quit_  # Exit program

print("You have {} guessed out of {} guesses.".format(len(guesses), total))
# should be the score, and the number of guesses shown
