from main import password_generator

#User Input Feature
welcom_message = """
Password Generator v1.0

The program is designed to generate a password 8-16 characteds consisting of unique and random characters from a pool of characters which will be defined based on your switch preferences.

"""
#For switch values checker wrt to user inputs
def user_input_switch_checker(user_input):
    if user_input in ['y', 'yes', 'true', '1']:
        return True
    elif user_input in ['n', 'no', 'false', '0']:
        return False
    else:
        raise ValueError("Invalid input: please enter yes or no")

length = input("Password Length: ")
easy_to_read = user_input_switch_checker(input("Enable Easy to Read Mode? (y/n): ").strip().lower())
if easy_to_read:
    esr_mode = input("Please choose easy to read mode (1-5): ").strip().lower()
else:
    esr_mode = 5

use_upper = user_input_switch_checker(input("Include uppercase char in password? (y/n): ").strip().lower())
use_digits = user_input_switch_checker(input("Include digits in password? (y/n): ").strip().lower())
use_special = user_input_switch_checker(input("Include special char in password? (y/n): ").strip().lower())

if length == "":
    print("Generated password:", password_generator(length=16, easy_to_read=easy_to_read, esr_mode=esr_mode, use_upper=use_upper, use_digits=use_digits, use_special=use_special))
else:
    print("Generated password:", password_generator(length=length, easy_to_read=easy_to_read, esr_mode=esr_mode, use_upper=use_upper, use_digits=use_digits, use_special=use_special))
