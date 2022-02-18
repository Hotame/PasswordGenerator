import random
import RPG

# Write Code 💻

print("Welcome To PyPassword Generator! ")

letters = int(input("How Many Letters Would You Like In The Password?\n"))
symbols = int(input("How Many Symbols Would You Like In The Password?\n"))
numbers = int(input("How Many Numbers Would You Like In The Password?\n"))

password = []

for letter in range(0, letters):
    letter = random.choice(RPG.combined_Letter)
    password.append(letter)

for symbol in range(0, symbols):
    symbol = random.choice(RPG.symbol)
    password.append(symbol)

for number in range(0, numbers):
    number = random.choice(RPG.number)
    password.append(number)

random.shuffle(password) # Shuffle The Password Characters.

print("".join(password))

    
