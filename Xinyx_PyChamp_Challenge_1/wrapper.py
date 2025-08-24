from main import password_generator

#For instructions, please refer to README.md in this repository
length = 16
use_upper = True
use_digits = True
use_special = True
easy_to_read = False
esr_mode = 5

print("Generated password:", password_generator(length=length, easy_to_read=easy_to_read, esr_mode=esr_mode, use_upper=use_upper, use_digits=use_digits, use_special=use_special))