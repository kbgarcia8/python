import ipywidgets as widgets
from IPython.display import display

#Widgets have their own display `repr` which allows them to be displayed using IPython's display framework. Constructing and returning an `IntSlider` automatically displays the widget
widgets.IntSlider()

#can also explicity display the widget using display()
w = widgets.IntSlider()
display(w)
display(w)
#Multiple display() call will make instances in sync

#closing widgets
w.close()

##WIDGET PROPERTIES
#Value 
w.value #display
w.value = 100 #set

#Keys
#widgets share `keys`, `description`, and `disabled`. 
w.keys #To see the entire list of synchronized, stateful properties of any specific widget, you can query the `keys` property.
"""
Widget Properties
_dom_classes - A list of CSS class names applied to the widget's DOM element; allows styling customization via frontend.
_model_module - Specifies the name of the JavaScript module that defines the model (usually '@jupyter-widgets/controls')
_model_module_version - Version of the model module; used for compatibility between frontend and backend.
_model_name - Name of the JavaScript model class this widget maps to (e.g., 'IntSliderModel')
_view_count - Internal counter of how many active views (rendered frontends) are attached to this widget
_view_module - JavaScript module name containing the view class (usually '@jupyter-widgets/controls')
_view_module_version - Version of the view module for compatibility with the Jupyter frontend.
_view_name - Name of the JavaScript view class (e.g., 'IntSliderView'); controls how the widget appears
behavior - (Rarely used; internal or deprecated) May define special behavior patterns for a widget
continuous_update - If True, the widget updates its value continuously (e.g., while dragging a slider); if False, only updates on release.
description - The label text displayed next to the widget in the UI.
description_allow_html - If True, HTML in the description will be rendered instead of escaped. Useful for rich formatting, but should be used cautiously.
disabled - If True, disables user interaction with the widget (greys it out in the UI).
layout - An instance of widgets.Layout used to control layout properties like width, margin, flex, etc.
max - The maximum allowed value (for widgets like sliders and numeric inputs).
min - The minimum allowed value.
orientation - Layout direction: 'horizontal' or 'vertical' (used in sliders and box containers).
readout - If True, shows the numeric value next to sliders; False hides it.
readout_format - A format string or specifier for how to display numeric readouts (e.g., '.2f' for two decimal places).
step - Increment step size for widgets like sliders or spinners (e.g., step of 1 or 0.1).
style - A style object (like SliderStyle) to customize visual aspects such as color, handle shape, etc. Can be used to view stylable attributes of current widget type
tabbable - True, the widget can be focused with the Tab key for accessibility.
tooltip - Text shown as a tooltip (hover text) when the user hovers over the widget.
value - The current value of the widget. This is the main data payload (e.g., slider position, text box content, selected item).
"""

#Setting widget properties
widgets.Text(value='Hello World!', disabled=True)

##LINKING TWO SIMILAR WIDGETS
"""
If you need to display the same value two different ways, you'll have to use two different widgets. Instead of attempting to manually synchronize the values of the two widgets, you can use the `link` or `jslink` function to link two properties together
"""
a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)

mylink = widgets.jslink((a, 'value'), (b, 'value'))
#unlink
mylink.unlink()