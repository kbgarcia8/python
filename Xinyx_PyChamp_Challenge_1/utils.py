import ipywidgets as widgets

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

#For switch values checker wrt to user inputs
def user_input_switch_checker(user_input):
    if user_input in ['y', 'yes', 'true', '1']:
        return True
    elif user_input in ['n', 'no', 'false', '0']:
        return False
    else:
        raise ValueError("Invalid input: please enter yes or no")
    
#Label widget creator
def label_generator(name, width):
    return widgets.HTML(
        value=f"""
            <div style="
                font-family: Arial;
                font-size: 1rem;
                font-weight: 700;
                display: flex;
                width: 100%;
                height: 100%;
                padding: 10px;
            ">
                {name}
            </div>
        """,
        layout=widgets.Layout(
            width=f'{width}%',
            height='100%'
        )
    )