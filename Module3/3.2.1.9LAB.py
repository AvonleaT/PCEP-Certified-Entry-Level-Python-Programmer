secret_exit_word = "chupacabra"
guess = input("Please guess a word (all lower case): ")
while guess != secret_exit_word:
    print("Try again")
    guess = input("Please guess a word (all lower case): ")

print("You've successfully left the loop.")