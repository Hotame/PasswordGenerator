import random
import RPGArt
from RPG import combined_Letter, all_symbols, all_numbers

# Write Code 💻

print("\n\nKaede : Welcome To PyPassword Generator! ")

letters = int(input("\n\nKaede : How Many Letters Would You Like In The Password -> "))
symbols = int(input("\n\nKaede : How Many Symbols Would You Like In The Password -> "))
numbers = int(input("\n\nKaede : How Many Numbers Would You Like In The Password -> "))

password = []

for letter in range(0, letters):
    letter = random.choice(combined_Letter)
    password.append(letter)

for symbol in range(0, symbols):
    symbol = random.choice(all_symbols)
    password.append(symbol)

for number in range(0, numbers):
    number = random.choice(all_numbers)
    password.append(number)

random.shuffle(password) # Shuffle The Password Characters.

print("\n\nKaede : " + "".join(password))
