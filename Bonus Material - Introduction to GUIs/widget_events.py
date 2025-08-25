import ipywidgets as widgets
from IPython.display import display
"""
The `on_click` method of the `Button` can be used to register a function to be called when the button is clicked. The docstring of the `on_click` can be seen below.
"""
#print(widgets.Button.on_click.__doc__)

#on_click
#button = widgets.Button(description="Click Me!")
#out = widgets.Output()

#def on_button_clicked(b):
#    with out:
#        print("Button clicked.")

#button.on_click(on_button_clicked)

#display(button, out)
#on_submit substitute - refer to .observe() below


#TRAITLET EVENTS
"""
Widget properties are IPython traitlets and traitlets are eventful. To handle changes, the `observe` method of the widget can be used to register a callback. The docstring for `observe` can be seen below.
"""
#print(widgets.Widget.observe.__doc__)
"""
It sets up a handler function that runs when a widget’s property (trait) changes.
Common traits: value, description, disabled, etc.

widget.observe(handler, names='value', type='change')

Parameter	Description
handler     A function that will be called when something changes
names	    What property you want to observe ('value', etc.)
type	    Type of event; usually 'change' (default)

🔧 The handler(change) function

This function receives a change dictionary with: (refer to Registering callbacks to trait changes in the kernel)

Key	Meaning
type	Type of event ('change', etc.)
owner	The widget that triggered the event
old	    The old value before the change
new	    The new value after the change
name	Which property changed (e.g. 'value')
"""

##Signatures
"""
Mentioned in the docstring, the callback registered must have the signature `handler(change)` where `handler` is the function and `change` is a dictionary holding the information about the change.

Using this method, an example of how to output an `IntSlider`'s value as it is changed can be seen below.
"""
import ipywidgets as widgets
from IPython.display import display

text = widgets.Text(description="Name")
out = widgets.Output()

def handle_submit(change):
    if change['type'] == 'change' and change['name'] == 'value':
        with out:
            out.clear_output()
            print(f"You entered: {change['new']}")

# Set up observation
text.observe(handle_submit, names='value') #Call handle_submit(change) every time the .value of this widget changes."
text.continuous_update = False  # prevents triggering on every keystroke

display(text, out)

##LINKING DIFF WIDGETS
import traitlets

# Create Caption
caption = widgets.Label(value = 'The values of slider1 and slider2 are synchronized')

# Create IntSliders
slider1 = widgets.IntSlider(description='Slider 1')
slider2 =  widgets.IntSlider(description='Slider 2')

# Use trailets to link
l = traitlets.link((slider1, 'value'), (slider2, 'value'))

# Display!
display(caption, slider1, slider2)

# Create Caption
caption = widgets.Label(value='Changes in source values are reflected in target1')

# Create Sliders
source = widgets.IntSlider(description='Source')
target1 = widgets.IntSlider(description='Target 1')

# Use dlink
dl = traitlets.dlink((source, 'value'), (target1, 'value'))
display(caption, source, target1)

# May get an error depending on order of cells being run!
l.unlink()
dl.unlink()

##Registering callbacks to trait changes in the kernel

caption = widgets.Label(value='The values of range1 and range2 are synchronized')
slider = widgets.IntSlider(min=-5, max=5, value=1, description='Slider')

def handle_slider_change(change):
    caption.value = 'The slider value is ' + (
        'negative' if change.new < 0 else 'nonnegative'
    )

slider.observe(handle_slider_change, names='value')

display(caption, slider)

##Linking widgets attributes from the client side
"""
When synchronizing traitlets attributes, you may experience a lag because of the latency due to the roundtrip to the server side. You can also directly link widget attributes in the browser using the link widgets, in either a unidirectional or a bidirectional fashion.

Javascript links persist when embedding widgets in html web pages without a kernel.
"""
# NO LAG VERSION
caption = widgets.Label(value = 'Changes in source_range values are reflected in target_range')

source_range = widgets.IntSlider(description='Source range')
target_range = widgets.IntSlider(description='Target range')

dl = widgets.jsdlink((source_range, 'value'), (target_range, 'value'))
display(caption, source_range, target_range)

#Difference between linking in the kernel and linking in the client - see 04-Widget Events

##CONTINUOUS UPDATE
"""
Some widgets offer a choice with their `continuous_update` attribute between continually updating values or only updating values when a user submits the value (for example, by pressing Enter or navigating away from the control).
"""

a = widgets.IntSlider(description="Delayed", continuous_update=False)
b = widgets.IntText(description="Delayed", continuous_update=False)
c = widgets.IntSlider(description="Continuous", continuous_update=True)
d = widgets.IntText(description="Continuous", continuous_update=True)

traitlets.link((a, 'value'), (b, 'value'))
traitlets.link((a, 'value'), (c, 'value'))
traitlets.link((a, 'value'), (d, 'value'))
widgets.VBox([a,b,c,d])
"""
Sliders, `Text`, and `Textarea` controls default to `continuous_update=True`. `IntText` and other text boxes for entering integer or float numbers default to `continuous_update=False` (since often you’ll want to type an entire number before submitting the value by pressing enter or navigating out of the box).
"""
