#widgets/GUI
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
#time recorder logic
import time
from datetime import datetime
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
        width='100%',
        height='37.5%'
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
        height='35%'
    )
)

#Tester name
tester_name_label = label_generator('Tester Name: ', 75, 100)
tester_name_widget = widgets.Text(
    disabled=False,
    placeholder='Name',
    layout=widgets.Layout(
        padding='10px',
        margin='10px 0px',
        width='100%',
        height='100%',
    )
)
tester_name=widgets.HBox(
    [tester_name_label, tester_name_widget],
    layout=widgets.Layout(width='100%',height='20%',display='flex',align_items='center',justify_content='flex-start',overflow='hidden')
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
    layout=widgets.Layout(width='100%',height='20%',display='flex',align_items='center',justify_content='flex-start',overflow='hidden')
)

#Button to generate text
generate_button = widgets.Button(
    description="Generate Text",
    layout=widgets.Layout(
        width="35%",
        height="15%",
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
        height="125%",
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
    layout=widgets.Layout(width='100%',height='150%',display='flex',align_items='center',justify_content='flex-start',overflow='hidden')
)

#Generate text to type
text_to_type=None
def generate_button_clicked(b):
    global start_time, end_time, text_to_type
    start_time, end_time = None, None
    typing_text_area_widget.value = ""
    typing_text_area_widget.focus()
    typing_text_area_widget.disabled=False

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

def start_timer_on_type(change):
    global start_time
    if start_time is None and change['new'].strip():
        start_time = time.time()

typing_text_area_widget.observe(start_timer_on_type, names="value")
#Submit
submit_instruction=label_generator("Click submit once done typing.", 75, 100)
#Button to submit entry
submit_button = widgets.Button(
    description="Submit",
    layout=widgets.Layout(
        width="35%",
        height="15%",
    ))
submit_button.add_class("submit-btn")
display(HTML("""
<style>
.submit-btn {
    background-color: #005A32 !important;
    border-radius: 12px !important;
    font-weight: 800;
    color: white !important;
}
</style>
"""))
# Submit handler
submit_output = widgets.Output(layout=widgets.Layout(
        border='3px double white',
        width="95%",
        height="15%",
        overflow='hidden'
))
file_created_output = widgets.Output(layout=widgets.Layout(
        border='3px double white',
        width="95%",
        height="5%",
        overflow='hidden'
))

def on_submit(b=None):
    global end_time
    end_time = time.time()
    user_text = typing_text_area_widget.value

    if not user_text.strip():
        display(HTML("<p style='color:red;'>❌ No text entered!</p>"))
        return
    
    #WPM calculation
    time_taken = end_time - start_time
    words = len(user_text.split())
    wpm = (words / time_taken) * 60

    #Accuracy calculation
    total_char = max(len(user_text), len(text_to_type))
    """
        - zip - pairs 2 variable element per element
        - list comprehension - out loop condition --> produce output 1 if element in loop satisfies condition
    """
    correct = sum(1 for a, b in zip(user_text, text_to_type) if a == b)
    accuracy = (correct / max(len(user_text), len(text_to_type))) * 100

    #Wrong chars
    """
        - enumerate - maps an index (i) for every item of your iterable (i, item_n)
        - list comprehension - out loop condition --> produce output (i, a, b) if element in loop satisfies condition
    """
    wrong_chars = [(i, a, b) for i, (a, b) in enumerate(zip(user_text, text_to_type)) if a != b]
    
    with submit_output:
        submit_output.clear_output()
        display(HTML(f"""
            <p>⏱ Time Taken: {time_taken:.2f}s</p>
            <p>⌨️ WPM: {wpm:.2f}</p>
            <p>🎯 Accuracy: {accuracy:.2f}%</p>
            <p>❌ Wrong chars: {wrong_chars}</p>
            <p>🕰️ Time created: {datetime.now()}</p>
        """))

    # Save results in a {tester_name}.txt
    with open(f"{tester_name_widget.value}.txt", "a") as result_file:
        result_file.write(f"WPM: {wpm:.2f}, Accuracy: {accuracy:.2f}%, Time: {time_taken:.2f}s\n Time Created: {datetime.now()}")
        with file_created_output:
            file_created_output.clear_output()
            display(HTML(f"""
                <div style='background-color: black; padding-inline: 2.5%; border: 2px double white; border-radius: 2.5%;'>
                    <p style='color: green; font-weight: bold;'>
                        ✅ Result printed and generated at {tester_name_widget.value}.txt
                    </p>
                </div>
            """))

submit_button.on_click(on_submit)

###FIX space for results

#Compile in 1 layout widget whole GUI
gui=widgets.VBox(
    [header,
    gui_description,
    tester_name,
    difficulty_select_dropdown,
    generate_button,
    text_to_type_output,
    typing_text_area,
    submit_instruction,
    submit_button,
    submit_output,
    file_created_output],
    layout=widgets.Layout(
        width='650px',
        height='1750px',
        margin='10px',
    )
)

display(gui)