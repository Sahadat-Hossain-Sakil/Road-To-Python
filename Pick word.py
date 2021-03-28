# Read a .txt file then
# Pick a random word from it.

import random

word_list = []

with open('sowpods.txt', 'r') as f:
    word_list = f.readlines()
    print("\n \tFile reading is complete !!")


# Randomly generate a word from word_list by using random.choice() or random.randit()

print("\n Random word :", random.choice(word_list))
# print("\n Random word :", word_list[random.randint(0, len(word_list))])