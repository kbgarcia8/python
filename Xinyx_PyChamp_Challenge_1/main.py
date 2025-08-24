import random #randomizer
import string #for character constants
import re # for regular expressions
from utils import int_check, boolean_check

#Main Function
def password_generator(length=16, easy_to_read=False, esr_mode=5, use_upper=True, use_digits=True, use_special=True):
    #Ensure atleast one use_ option is enabled to increase password strength
    if not use_upper and not use_digits and not use_special:
        raise ValueError("At least one character type must be enabled (uppercase, digits, or special characters).")
    
    #Ensure argument types
    length = int_check('length',length)
    esr_mode = int_check('esr_mode',esr_mode)
    boolean_check('easy_to_read', easy_to_read)
    boolean_check('use_upper', use_upper)
    boolean_check('use_digits', use_digits)
    boolean_check('use_special', use_special)
    


    #Ensure password lenght min: 8 and max: 16
    if length < 8 or length > 16:
        raise ValueError("Password must between 8 and 16 characters.")
    
    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_upper else '' #Tenary operation (1 line if-else statement): <value if true> if condition else <value if false>
    digits = string.digits if use_digits else ''
    special = '!@#$%^&*()' if use_special else ''
    
    if easy_to_read:
        if not use_digits and not use_special:
            raise AssertionError("Either use_digits and use_special option must be enabled if easy_to_read is enabled")
        #min_main_length is reserved for uppercase or lowercase. This is to ensure password will not be digits/special characters in majority
        min_main_length = 4
        max_digits_or_special = length - min_main_length

        if max_digits_or_special < 0 or min_main_length < 4:
            raise ValueError("Length too short for easy-to-read mode.")
        
        # Randomly decide how many digits and specials to put (total max_extra)
        num_digits = random.randint(0, max_digits_or_special if use_digits else 0)
        num_special = random.randint(0, max_digits_or_special - num_digits if use_special else 0)
        main_length = length - (num_digits + num_special)

        # Adjust counts to ensure main length meets minimum and digits/specials do not exceed limits.
        # Repeat adjustments until all constraints are satisfied.
        while main_length < min_main_length or num_digits > 10 or num_special > 10:
            main_length = max(main_length, min_main_length)
            extra = length - main_length

            num_digits = min(num_digits, 10, extra)
            num_special = min(num_special, 10, extra - num_digits)

            total_used = main_length + num_digits + num_special
            if total_used < length:
                main_length += (length - total_used)

        # Build core with letters only
        main_chars = lowercase + uppercase
        if not main_chars:
            raise ValueError("At least one of use_upper or lowercase must be True for easy-to-read mode.")
        
        password_main = random.sample(main_chars, k=main_length)

        # Build digits and special chars pools
        digit_chars = random.sample(digits, k=num_digits) if use_digits else []
        special_chars = random.sample(special, k=num_special) if use_special else []
        # else [] to ensure variables will not be undefined and is always a list
        #For special characters
        if esr_mode < 1 or esr_mode > 5:
            raise ValueError("esr_mode has only modes 1-5.")
        
        extras = digit_chars + special_chars
        #Shuffle characters
        random.shuffle(extras)
        random.shuffle(password_main)
        random.shuffle(digit_chars)
        random.shuffle(special_chars)
        if esr_mode == 5:
            if random.choice([True, False]):
                # Extras at start
                password = extras + password_main
            else:
                # Extras at end
                password = password_main + extras
        elif esr_mode == 4:
            # Extras at end
            password = password_main + extras
        elif esr_mode == 3:
            # Extras at start
            password = extras + password_main
        elif esr_mode == 2: 
            # Digits at start and special chars at end
            password = digit_chars + password_main + special_chars
        elif esr_mode == 1:
            # Special chars at start and digits at end
            password = special_chars + password_main + digit_chars
        else:
             raise ValueError("esr_mode has only modes 1-5.")
        
        return ''.join(password)

    else:
        #Concatenate all characters allowed
        all_chars = list(lowercase + uppercase + digits + special)

        #Ensure all_chars has atleast one character set incase of code/module bug
        if not all_chars:
            raise ValueError("At least one character set must be selected.")
        
        #Ensure that all_chars to be exhausted are always greater than length
        if length > len(all_chars):
            raise ValueError(f"Length {length} is too long for the selected character sets (max {len(all_chars)}).")

        #Ensure the password has at least one character from each selected category
        password = []
        #When a character has been appended it will be removed from the all_chars list to avoid repeated characters
        if use_upper:
            choosen_upper = random.choice(uppercase)
            password.append(choosen_upper)
            all_chars.remove(choosen_upper)
        if use_digits:
            choosen_digit = random.choice(digits)
            password.append(choosen_digit)
            all_chars.remove(choosen_digit)
        if use_special:
            choosen_special = random.choice(special)
            password.append(choosen_special)
            all_chars.remove(choosen_special)
        
        choosen_lower = random.choice(lowercase)
        password.append(choosen_lower)
        all_chars.remove(choosen_lower)

        #Randomly fill rest of the password wrt length requirement
        while len(password) < length:
            choosen_char = random.choice(all_chars)
            password.append(choosen_char)
            all_chars.remove(choosen_char)
        
        #Re-shuffle characters added
        random.shuffle(password)
        return ''.join(password)



    