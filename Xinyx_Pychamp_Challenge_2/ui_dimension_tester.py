# --- Imports ---
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
import time
import ipyevents
from datetime import datetime
from utils import label_generator, random_text_generator

# --- Header / Branding ---
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
        height='7.5%'
    )
)
# --- Welcome Message ---
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
        height='25%'
    )
)

# --- Tester Name ---
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
    layout=widgets.Layout(width='100%',height='3.5%',display='flex',align_items='center',justify_content='flex-start',overflow='hidden')
)


# --- Difficulty Selection ---
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
    layout=widgets.Layout(width='100%',height='3.5%',display='flex',align_items='center',justify_content='flex-start',overflow='hidden')
)

# --- Generate Button ---
generate_button = widgets.Button(
    description="Generate Text",
    disabled=False,
    layout=widgets.Layout(
        width="35%",
        height="3.5%",
        margin="5px 0px"
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
# --- Output: Text to Type ---
text_to_type_output = widgets.Output(layout=widgets.Layout(
        border='3px double black',
        width="95%",
        height="25%",
        overflow='hidden'
))

# --- Typing Area ---
typing_text_area_label = label_generator('Type here: ', 75, 10)
typing_text_area_widget = widgets.Textarea(
    disabled=True,
    placeholder='Start typing test',
    layout=widgets.Layout(
        padding='10px 0px',
        width='95%',
        height='100%',
    )
)
display(HTML("""
<style>
.no-resize textarea {
    resize: none !important;
    font-size: 1rem;
}
</style>
"""))
typing_text_area_widget.add_class("no-resize")
typing_text_area=widgets.VBox(
    [typing_text_area_label, typing_text_area_widget],
    layout=widgets.Layout(width='100%',height='20%',display='flex',align_items='flex-start',justify_content='flex-start',overflow='hidden')
)

# --- Generate Text Handler ---
text_to_type=None
def generate_button_clicked(b):
    global start_time, end_time, text_to_type
    start_time, end_time = None, None
    typing_text_area_widget.value = ""
    typing_text_area_widget.focus()
    typing_text_area_widget.disabled=False
    generate_button.disabled=True
    retry_button.disabled=True
    retry_button.display="none"

    with text_to_type_output:
        clear_output(wait=True)
        try:
            text_to_type = random_text_generator(level=difficulty_select_dropdown_widget.value)
            display(HTML(f"""
                <div style='background-color: #F1EE8E; padding-inline: 2.5%; border: 2px double white; height: 500px;'>
                    <p style='color: black; font-weight: bold; text-decoration: underline; font-size: 1.25rem;'>⌨️ Text to type: </p>
                    <span style='font-weight: 500; color: black; font-size: 1rem;'>{text_to_type}</span>
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

generate_button.on_click(generate_button_clicked)

# --- Timer Start ---
start_time, end_time = None, None

def start_timer_on_type(change):
    global start_time
    if start_time is None and change['new'].strip():
        start_time = time.time()

typing_text_area_widget.observe(start_timer_on_type, names="value")
# --- Submission Instructions ---
submit_instruction=label_generator("Press Ctrl+Shift+Enter to submit once done.", 75, 3.5)

# --- Result / File Outputs ---
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

with submit_output:
    submit_output.clear_output()
    display(HTML(f"""
        <div style='background-color: #E69B00; padding-inline: 2.5%; border: 2px double white; border-radius: 2.5%; font-size: 1rem; color: whitesmoke; font-weight: 700;'>
            <p>⏱ <u><b>Time Taken:</b></u> {00.00}s</p>
            <p>⌨️ <u><b>WPM:</b></u> {00.00}</p>
            <p>🎯 <u><b>Accuracy:</b></u> {00.00}%</p>
            <p>❌ <u><b>Wrong chars:</b></u> {0000}</p>
            <p>🕰️ <u><b>Time created:</b></u> {'2025-08-29 20:53:17'}</p>
        </div>
    """))

with file_created_output:
    file_created_output.clear_output()
    display(HTML(f"""
        <div style='background-color: black; padding-inline: 2.5%; border: 2px double white; border-radius: 2.5%;'>
            <p style='color: green; font-weight: bold;'>
                ✅ Result printed and generated at result.txt
            </p>
        </div>
    """))

# --- Retry Button ---
retry_button = widgets.Button(
    description="Retry Typing",
    disabled=False,
    display='block',
    layout=widgets.Layout(
        width="35%",
        height="3.5%",
        margin="5px 0px"
    ))
retry_button.add_class("retry-btn")
display(HTML("""
<style>
.retry-btn {
    background-color: #DF705F !important;
    border-radius: 12px !important;
    font-weight: 800;
    color: whitesmoke !important;
}
</style>
"""))

retry_button.on_click(generate_button_clicked)


# --- GUI Assembly ---
gui=widgets.VBox(
    [
        header,
        gui_description,
        tester_name,
        difficulty_select_dropdown,
        generate_button,
        text_to_type_output,
        typing_text_area,
        submit_instruction,
        submit_output,
        file_created_output,
        retry_button
    ],
    layout=widgets.Layout(
        width='650px',
        height='2250px',
        margin='10px',
    )
)

display(gui)