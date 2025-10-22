#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def user_input():
    while True:
        try:
            user_input = input("Please enter a value:\n")
            user_input_int = int(user_input) 
            if (user_input_int > 0):
                print("Calculating Fibonacci Sequence")
                return user_input_int
                break
            else:
                print("Invalid number, try agian")

        except ValueError:
            print("Invalid input.")
        
def calc_sequence(num):
    a, b = 0, 1
    print(a)
    print(b)
    for _ in range(2, num):  # Start from the 3rd term
        next_term = a + b
        print(next_term)
        a = b
        b = next_term
    return ""
        
def print_sequence(num):
    a, b = 0,1
    if (num == 1):
        print(a)
    elif (num == 2):
        print(a,b)
    else:
        print(calc_sequence(num))
        
num = user_input()
print_sequence(num)
