#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
     if (username.lower() == "admin") and (password == "12345"):  # .lower() for case-insensitivity
        return "Access granted"
     else:
        return "Access denied"
    

def hows_the_weather(temperature):
    # your code here
     if temperature < 40:
        return "It's brisk out there!"
     elif 40 <= temperature < 65:
        return "It's a little chilly out there!"
     elif temperature > 85:
        return "It's too dang hot out there!"
     else:
        return "It's perfect out there!"



def fizzbuzz(number):
    # your code here
     if number % 15 == 0:    # Check divisibility by 15 first (both 3 and 5)
        return "FizzBuzz"
     elif number % 3 == 0:
        return "Fizz"
     elif number % 5 == 0:
        return "Buzz"
     else:
        return number


def calculator(operation, num1, num2):
    # your code here
    if operation == '+':
        return num1 + num2 
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print('Invalid operation!')
        return None

    