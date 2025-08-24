#For switch/argument values checker inside the function
def boolean_check(name, val):
    if isinstance(val, bool):
        return
    raise ValueError(f"{name} must be a boolean (True or False)")

def int_check(name, val):
    if not isinstance(val, int):
        try:
            return int(val)
        except ValueError:
            raise ValueError(f"{name} must be a digit.")
    return val