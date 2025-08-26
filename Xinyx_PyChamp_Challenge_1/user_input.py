from main import password_generator
from utils import user_input_switch_checker

#User Input Feature
welcome_message = """
Password Generator v1.0

The program is designed to generate a password 8-16 characteds consisting of unique and random characters from a pool of characters which will be defined based on your switch preferences.

"""

print(welcome_message)

esr_mode_selection_message="""

"""

while True:
    try:
        length = input("Password Length: ")
        easy_to_read = user_input_switch_checker(input("Enable Easy to Read Mode? (y/n): ").strip().lower())
        if easy_to_read:

            esr_mode = input("Please choose easy to read mode (1-5): \n[1: special + main + digits; \n2: digits + main + special; \n3: (special + digits) + main; \n4: main + (special + digits) \n5: Randomly start or end]").strip().lower()
        else:
            esr_mode = 5

        use_upper = user_input_switch_checker(input("Include uppercase char in password? (y/n): ").strip().lower())
        use_digits = user_input_switch_checker(input("Include digits in password? (y/n): ").strip().lower())
        use_special = user_input_switch_checker(input("Include special char in password? (y/n): ").strip().lower())

        if length == "":
            length=16
        else:
            length=int(length)

        password=password_generator(length=length, easy_to_read=easy_to_read, esr_mode=esr_mode, use_upper=use_upper, use_digits=use_digits, use_special=use_special)

        print("\n Generated Password: ",password)
        break

    except (ValueError, AssertionError) as e:
        print(f"\nERROR: {e}")
        print("***Please fill up the inputs properly.***\n")