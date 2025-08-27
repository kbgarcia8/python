#widgets/GUI
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
#utils
from utils import label_generator, random_text_generator



#Header/descriptions
gui_logo_file = open("images/typing_test_2.png", "rb")
gui_logo_read = gui_logo_file.read()
gui_logo = widgets.Image(
    value=gui_logo_read,
    format='png',
    layout=widgets.Layout(width='25%', height='95%')
)
gui_title = widgets.HTML(
    value="""
    <div style="font-family: Arial; border-radius: 2.5%; border: 3.5px solid #FE8D01; background-color: #FFB668; color: whitesmoke; display: flex; align-items: center; justify-content: center; flex-direction: column;">
        <h2>Typing Test v1.0</h2>
    </div>
    """,
    layout=widgets.Layout(
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
welcome_message = """
This program will test your typing skills by giving you a passage to type.
    - Once you start typing, the timer begins.

When you finish, the program will calculate:
   - ⏱️ Time Taken
   - ⚡ Words Per Minute (WPM)
   - 🎯 Accuracy (how close your text matches the original)

✨ Bonus Features:
- See which characters you got wrong
- Retry the test for a better score
- Save your results (WPM, accuracy, etc.) to a text file

Good luck, and type your best!
"""
gui_description = widgets.HTML(
    value=f"""
    <div style="font-family: Arial; border-radius: 1.25%; border: 3.5px double white; background-color: #EBEBEB; color: black; display: flex; align-items: center; justify-content: center; flex-direction: column; padding: 2.5%;">
        <p style="white-space: pre; text-align: left; width: 100%; font-weight: 700;">{welcome_message}</p>
    </div>
    """,
    layout=widgets.Layout(
        border='2px double black',
        padding='10px',
        margin='10px 0px',
        width='100%',
        height='25.75%'
    )
)

#difficulty select
difficulty_select_dropdown_label = label_generator('Select difficulty: ', 75, 100)
difficulty_select_dropdown_widget = widgets.Dropdown(
    options={'Easy (short)': 'easy', 'Normal': 'normal', 'Hard (long)': 'hard'},
    value='easy',
    disabled=False,
    layout=widgets.Layout(
        padding='10px',
        margin='10px 0px',
        width='75%',
        height='100%',
    )
)
difficulty_select_dropdown=widgets.HBox(
    [difficulty_select_dropdown_label, difficulty_select_dropdown_widget],
    layout=widgets.Layout(width='100%',height='2.5%',display='flex',align_items='center',justify_content='flex-start',overflow='hidden')
)

#Button to generate text
generate_button = widgets.Button(
    description="Generate Text",
    layout=widgets.Layout(
        width="35%",
        height="50px",
    ))
generate_button.add_class("custom-btn")
display(HTML("""
<style>
.custom-btn {
    background-color: #FFA630 !important;
    border-radius: 12px !important;
    font-weight: 800;
    color: white !important;
}
</style>
"""))
#Button clicked handler
text_to_type_output = widgets.Output(layout=widgets.Layout(
        border='3px double white',
        width="95%",
        height="15%",
        overflow='hidden'
))

#typing text area
typing_text_area_label = label_generator('Type here: ', 100, 25)
typing_text_area_widget = widgets.Textarea(
    disabled=True,
    placeholder='Start typing test',
    layout=widgets.Layout(
        padding='10px',
        margin='10px 0px',
        width='100%',
        height='100%',
    )
)
display(HTML("""
<style>
.no-resize textarea {
    resize: none !important;
}
</style>
"""))
typing_text_area_widget.add_class("no-resize")
typing_text_area=widgets.VBox(
    [typing_text_area_label, typing_text_area_widget],
    layout=widgets.Layout(width='100%',height='15%',display='flex',align_items='center',justify_content='flex-start',overflow='hidden')
)

text_to_type=None
def generate_button_clicked(b):
    with text_to_type_output:
        clear_output(wait=True)
        try:
            text_to_type = random_text_generator(level=difficulty_select_dropdown_widget.value)
            display(HTML(f"""
                <div style='background-color: black; padding-inline: 2.5%; border: 2px double white; border-radius: 2.5%; height: 290px;'>
                    <p style='color: whitesmoke; font-weight: bold; text-decration: underline;'>⌨️ Text to type: </p>
                    <span style='font-weight: 700; color: white; font-size: 0.75rem;'>{text_to_type}</span>
                </div>
            """))
            typing_text_area_widget.disabled=False

        except (ValueError, AssertionError) as e:
            display(HTML(f"""
                <divW style='background-color: black; padding: 1.25%; border: 2px double white; border-radius: 2.5%; font-size: 0.75rem;'>
                    <p style='color: red; font-weight: bold;'>❌ Error: 
                        <span style='font-weight: 700; color: white;'>{e}</span>
                    </p>
                </div>
            """))

#Assign handler to generate button
generate_button.on_click(generate_button_clicked)

### TYPING CALCULATIONS ###
start_time, end_time = None, None
#continue here

#Compile in 1 layout widget whole GUI
gui=widgets.VBox(
    [header,gui_description,difficulty_select_dropdown,generate_button,text_to_type_output,typing_text_area],
    layout=widgets.Layout(
        width='650px',
        height='2000px',
        margin='10px',
    )
)

display(gui)