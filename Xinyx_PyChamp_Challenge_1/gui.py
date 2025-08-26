import ipywidgets as widgets
from IPython.display import display, HTML
from utils import label_generator
from main import password_generator

#Header/descriptions
gui_logo_file = open("images/password.png", "rb")
gui_logo_read = gui_logo_file.read()
gui_logo = widgets.Image(
    value=gui_logo_read,
    format='png',
    layout=widgets.Layout(width='25%', height='95%')
)

gui_title = widgets.HTML(
    value="""
    <div style="font-family: Arial; border-radius: 2.5%; border: 3.5px solid #003A6B; background-color: #3776A1; color: whitesmoke; display: flex; align-items: center; justify-content: center; flex-direction: column;">
        <h2>Password Generator v1.0</h2>
    </div>
    """,
    layout=widgets.Layout(
        border='solid 3px black',
        padding='10px',
        margin='10px 0px',
        width='75%',
        height='65%'
    )
)

header=widgets.HBox(
    [gui_logo,gui_title],
    layout=widgets.Layout(
        width='100%'
    )
)

welcome_message = 'The program is designed to generate a password 8-16 characteds consisting of unique and random characters from a pool of characters which will be defined based on your switch preferences.'

gui_description = widgets.HTML(
    value=f"""
    <div style="font-family: Arial; border-radius: 2.5%; border: 3.5px double white; background-color: black; color: whitesmoke; display: flex; align-items: center; justify-content: center; flex-direction: column; padding: 2.5%;">
        <p>{welcome_message}</p>
    </div>
    """,
    layout=widgets.Layout(
        border='solid 3px black',
        padding='10px',
        margin='10px 0px',
        width='100%',
        height='20%'
    )
)
#Recurring layout
options_layout=widgets.Layout(width='100%',height='10%',display='flex',align_items='center',justify_content='flex-start',overflow='hidden')

#Password length
password_length_label = label_generator('Password Length: ', 25)
password_length_widget = widgets.IntSlider(
    value=16,
    min=8,
    max=16,
    step=1,
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d',
    layout=widgets.Layout(
        padding='10px',
        margin='10px 0px',
        width='50%',
        height='100%'
    )
)
password_length=widgets.HBox(
    [password_length_label,password_length_widget],
    layout=options_layout
)
#Easy-to-read mode
easy_to_read_checkbox_label = label_generator('Enable Easy-to-read-mode? ', 75)
easy_to_read_checkbox_widget = widgets.Checkbox(
    value=False,
    disabled=False,
    orientation='horizontal',
    layout=widgets.Layout(
        padding='10px',
        margin='10px 0px',
        width='75%',
        height='100%'
    )
)
easy_to_read_checkbox=widgets.HBox(
    [easy_to_read_checkbox_label,easy_to_read_checkbox_widget],
    layout=options_layout
)
#easy_to_read_mode
easy_to_read_dropdown_label = label_generator('Select easy-to-read mode: ', 75)
easy_to_read_dropdown_widget = widgets.Dropdown(
    options={'1: special + main + digits': 1, '2: digits + main + special': 2, '3: (special + digits) + main': 3, 'main + (special + digits)': 4, '5: Randomly start or end': 5},
    value=5,
    disabled=True,
    layout=widgets.Layout(
        padding='10px',
        margin='10px 0px',
        width='75%',
        height='100%',
    )
)
easy_to_read_dropdown=widgets.HBox(
    [easy_to_read_dropdown_label,easy_to_read_dropdown_widget],
    layout=options_layout
)


#Make easy_to_read_mode disabled depending on easy_to_read value
def toggle_dropdown(change):
    easy_to_read_dropdown_widget.disabled = not change['new']

easy_to_read_checkbox_widget.observe(toggle_dropdown, names="value") #every time easy_to_read_checkbox_widget changes toggle_dropdown runs

#Include uppercase
include_uppercase_label = label_generator('Include uppercase char in password? ', 75)
include_uppercase_widget = widgets.Checkbox(
    value=False,
    disabled=False,
    orientation='horizontal',
    layout=widgets.Layout(
        padding='10px',
        margin='10px 0px',
        width='75%',
        height='100%'
    )
)
include_uppercase=widgets.HBox(
    [include_uppercase_label,include_uppercase_widget],
    layout=options_layout
)
#Include digits
include_digits_label = label_generator('Include digits in password? ', 75)
include_digits_widget = widgets.Checkbox(
    value=False,
    disabled=False,
    orientation='horizontal',
    layout=widgets.Layout(
        padding='10px',
        margin='10px 0px',
        width='75%',
        height='100%'
    )
)
include_digits=widgets.HBox(
    [include_digits_label,include_digits_widget],
    layout=widgets.Layout(
        width='100%',
        height='10%',
        display='flex',
        align_items='center',
        justify_content='flex-start',
        overflow='hidden'
    )
)
#Include special char
include_special_char_label = label_generator('Include special char in password? ', 75)
include_special_char_widget = widgets.Checkbox(
    value=False,
    disabled=False,
    orientation='horizontal',
    layout=widgets.Layout(
        padding='10px',
        margin='10px 0px',
        width='75%',
        height='100%'
    )
)
include_special_char=widgets.HBox(
    [include_special_char_label,include_special_char_widget],
    layout=options_layout
)
#Submit button - to execute password generator
submit_button = widgets.Button(
    description="Generate Password",
    layout=widgets.Layout(
        width="35%",
        height="50px",
    ))
submit_button.add_class("custom-btn")
display(HTML("""
<style>
.custom-btn {
    background-color: #003A6B !important;
    border-radius: 12px !important;
    font-weight: 800;
    color: white !important;
}
</style>
"""))

# Button click handler
output = widgets.Output(layout=widgets.Layout(
        border='3px double white',
        width="95S%",
        height="7.5%",
        overflow='hidden'
))
def on_submit_clicked(b):
    output.clear_output()  # clear previous output
    with output:
        try:
            password = password_generator(
                length=password_length_widget.value,
                easy_to_read=easy_to_read_checkbox_widget.value,
                esr_mode=easy_to_read_dropdown_widget.value,
                use_upper=include_uppercase_widget.value,
                use_digits=include_digits_widget.value,
                use_special=include_special_char_widget.value,
            )
            display(HTML(f"""
                    <div style='background-color: black; padding-inline: 2.5%; border: 2px double white; border-radius: 2.5%;'>
                        <p style='color: green; font-weight: bold;'>
                            ✅ Generated password: 
                            <span style='font-weight: 700; color: white; '>{password}</span>
                        </p>
                    </div>
                    """))
        except (ValueError, AssertionError) as e:
            display(HTML(f"""
                    <div style='background-color: black; padding: 1.25%; border: 2px double white; border-radius: 2.5%; font-size: 0.75rem;'>
                        <p style='color: red; font-weight: bold;'>❌ Error: 
                            <span style='font-weight: 700; color: white;'>{e}</span>
                        </p>
                    </div>
                    """))
            print(f"⚠️ Error: {e}")

submit_button.on_click(on_submit_clicked) #assign event handler to button on_click

#Compile in 1 layout widget whole GUI
gui=widgets.VBox(
    [header,gui_description,password_length,easy_to_read_checkbox,easy_to_read_dropdown,include_uppercase,include_digits,include_special_char,submit_button,output],
    layout=widgets.Layout(
        width='650px',
        height='900px',
        margin='10px',
    )
)

display(gui)