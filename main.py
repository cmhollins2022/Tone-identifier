import requests
import re


# Task: In the simplest and most efficient way possible, create a program that identifies the tone of a given file
# or text block, based on key words.

# Practicality: This could be a good way to quickly identify the tone and overall feel of someone's writing. The use
# wouldn't necessarily have to stop there. It could be used to (possibly) suggest replacements for words. A
# functionality similar to the "Grammarly" application.

# Pseudocode: First Steps

# Step 1: After a file or list of words is entered, break up the words, and enter them into a list. Do not include
# any form of punctuation. The list should be purely made up of the words from the text.

# Main file function that allows words to be broken up into individual strings,
# remove punctuation, then appended to a list:

# Original way to remove punctuation:
# def read_and_store_text(file_name):
#     file = open(file_name, "r", encoding='utf-8-sig')
#     divided_file_words = str(file.read()).lower().replace('”', '').replace('“', '').replace(',', '').replace(
#         '.' or '?' or '!', '').split()
#
#     return print(divided_file_words)
#
#
# read_and_store_text("sample-text.txt")

# Revised way to list and store only words. (Using ReGex)
def read_and_store_text(file_name):
    file = open(file_name, "r", encoding='utf-8-sig')
    divided_text = str(file.read())
    retrieve_only_words = re.sub(".", "", divided_text)

    return print(divided_text)


def regex_test():
    string_text = 'I am trying to remove the "punctuation??" from this string!'
    x = re.sub("")


read_and_store_text("sample-text.txt")


# Querying the dictionary API... going to explore more strategies and options soon.
# Idea Alert: Having 5 synonyms of each word both positive and negative... within a list...
# then, an algorithm could query the API to see if any of the 5 (or more, depending on how accurate
# or specific we would like to be) can check to see if the words are contained in the
# "Synonym" array or list of words (for the given word within the API)

# For front end, you could even have an option to possibly give a definition of the word when clicked.
def identify_tone_of_word():
    access_api = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/hello")

    return print(access_api.json())


identify_tone_of_word()