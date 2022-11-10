import re
import json
import string

import requests


# Task: In the simplest and most efficient way possible, create a program that identifies the tone of a given file
# or text block, based on key words.

# Practicality: This could be a good way to quickly identify the tone and overall feel of someone's writing. The use
# wouldn't necessarily have to stop there. It could be used to (possibly) suggest replacements for words. A
# functionality similar to the "Grammarly" application.

# Pseudocode: First Steps

# 1 - After a file or list of words is entered, break up the words, and enter them into a list. Do not include
# any form of punctuation. The list should be purely made up of the words from the text.

# 2 - Define "Positive" and "Negative" somehow...

# Main file function that allows words to be broken up into individual strings,
# remove punctuation, then appended to a list:

# Querying the dictionary API... going to explore more strategies and options soon.
# Idea: Having 5 synonyms of each word both positive and negative... within a list...
# then, an algorithm could query the API to see if any of the 5 (or more, depending on how accurate
# or specific we would like to be) can check to see if the words are contained in the
# "Synonym" array or list of words (for the given word within the API)
# For front end, you could even have an option to possibly give a definition of the word when clicked.

# Natural language processing - IBM...

# RegEx strategies...

def read_and_store_text(file_name):
    new_words_list = []
    string_and_read_file = open(file_name, "r",
                                encoding='utf-8-sig').read().split()  # open, read and convert the file into a list
    for word in string_and_read_file:  # iterate through each of the list items
        isolated_word = re.sub(r'[^\w\s]', '', word)  # remove everything except for letters
        new_words_list.append(isolated_word)  # add each isolated word into the new list
    return print(new_words_list)


read_and_store_text("sample-text.txt")


def synonyms_list(word: str):
    new_list = []
    thesaurus_api_data = requests.get(
        f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}"
        f"?key=457b0e9d-88b8-470d-b118-a7d41baa1d92").json()
    print(thesaurus_api_data['meta'])


synonyms_list("happy")
