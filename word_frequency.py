#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sent():
    user_sentence = input("Enter a sentence: ")

    while (is_sentence(user_sentence) == False):
        print("This does not meet the criteria for a sentence.")
        user_sentence = input("Enter a sentence: ")
        
    return user_sentence

def calc_fequences(sentence):
    sent = re.sub(r'[^\w\s]', '', sentence).lower()
    words = sent.split()
    
    list_word = []
    frequencies = []
    
    for word in words:
        if word in list_word:
            index = list_word.index(word)
            frequencies[index] += 1
        else:
            list_word.append(word)
            frequencies.append(1)
        
    return list_word, frequencies
        
def print_fre(list_word, frequencies):
    for i in range(len(list_word)):
        print(f"{list_word[i]}: {frequencies[i]}")
        
def main():
    user_sentence = get_sent()
    list_word, frequencies = calc_fequences(user_sentence) 
    print_fre(list_word, frequencies)
    
main()
    

