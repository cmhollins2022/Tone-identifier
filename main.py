# Task: In the simplest and most efficient way possible, create a program that identifies the tone of a given file
# or text block, based on keywords.

# Practicality: This could be a good way to quickly identify the tone and overall feel of someone's writing. The use
# wouldn't necessarily have to stop there. It could be used to (possibly) suggest replacements for words. A
# functionality similar to the "Grammarly" application.

# Pseudocode: First Steps

# Step 1: After a file (or list) of words is entered, break up the words, and enter them into a list. Do not include
# any form of punctuation. The list should be purely made up of the words from the text.

# Main file function that allows words to be broken up into individual strings,
# remove punctuation, then appended to a list:
def read_and_store_text(file_name):
    file = open(file_name, "r", encoding='utf-8-sig')
    divided_file_words = str(file.read()).lower().replace('”', '').replace('“', '').replace(',', '').replace(
        '.' or '?' or '!', '').split()

    return print(divided_file_words)


read_and_store_text("sample-text.txt")
