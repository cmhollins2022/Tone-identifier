# Task: In the simplest and most efficient way possible, create a program that takes in a string of words, or
# that can read a file, then using either a given list of words (for each tone), or a machine learning algorithm,
# dictate the tone of the given passage.

# Practicality: This could be a good way to quickly identify the tone and overall feel of someone's writing. The use
# wouldn't necessarily have to stop there. It could be used to (possibly) suggest replacements for words. A
# functionality similar to the "Grammarly" application.

#: Possible Use Cases:

# Pseudocode: First Steps

# Step 1: After a file or list of words is entered, break up the words, and enter them into a list. Do not include
# any form of punctuation. The list should be purely made up of words.

# We will need a function that takes in a list of words, or that can read a file and break it up into a list of words.
# (The other possible case could be a front end set-up that allows a user to enter in text through a text through a text
# Block, then the back-end would stringify and append the words to a list, allowing them to be analyzed further.

# Main file function that allows words to be broken up into individual strings,
# remove punctuation, then appended to a list:
def read_and_store_text(file_name):
    file = open(file_name, "r", encoding='utf-8-sig')
    divided_file_words = str(file.read()).replace("." or "?" or "!", "").split()

    return print(divided_file_words)


read_and_store_text("sample-text.txt")
