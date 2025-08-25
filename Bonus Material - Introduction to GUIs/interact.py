from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display

# Very basic function
def f(x):
    print("Hello")
    return x
##2nd argument is called widget abbreviation
# Generate a slider to interact with
interact(f, x=10,);
interact(f, x=(0,4));#2-tuple (min,max)
interact(f, x=(0,8,2));#3-tuple (min,max,step)
interact(f, x=(0.0,10.0)); #float-slider default step is 0.1
#integer and float-valued slider can pucj initial value by passing default argument to underlying function
@interact(x=(0.0,20.0,0.5))
def h(x=5.5):
    return x
# Booleans generate check-boxes
interact(f, x=True);
# Strings generate text areas
interact(f, x='Hi there!');
#Dropdown
interact(f, x=['orange','apple']); #list, only passes string values to your function
interact(f, x={'one':1, 'two': 2}); #dict if you want to pass non-string values to your function
"""
`interact` can also be used as a decorator. This allows you to define a function and interact with it in a single shot. As this example shows, `interact` also works with functions that have multiple arguments.z
"""
#@interact(x=True, y=1.0)
#def g(x, y):
#    return (x, y)

#Fixed arguments
def h(mode, q):
    return (mode, q)

interact(h, mode=5, q=fixed(20));

#Widget abbreviations
"""
When you pass an integer-valued keyword argument of `10` (`x=10`) to `interact`, it generates an integer-valued slider control with a range of `[-10,+3\times10]`. In this case, `10` is an *abbreviation* for an actual slider widget:

IntSlider(min=-10,max=30,step=1,value=10)

In fact, we can get the same result if we pass this `IntSlider` as the keyword argument for `x`:
"""
# Can call the IntSlider to get more specific
interact(f, x=widgets.IntSlider(min=-10,max=30,step=1,value=5));

#function annotations - similar to type annotattion in type script
def f(x:True):  # Python 3 only
    return x

#OR if you dint want a default value just a type
def f(x:True):  # Python 3 only
    return x


#Since widget abbreviation has already been define, no need to call it in interact
interact(f);

#interactive function
"""
Useful when you want to reuse the widgets that are produced or access the data that is bound to UI controls

Unlike interact, return value of function will not be displayed automatically. You can display a value inside the function with IPython.display.display
"""
def f(a, b):
    display(a + b) #display to show output everytime widget changes
    return a+b

#unlike interact and interactive returns a Widget instance rather than displaying it immediately
w = interactive(f, a=10, b=20)
type(w) #data type is ipywidgets.widgets.interaction.interactive, a subclass of VBox a container of other widgets
"""
The children of the `interactive` are two integer-valued sliders and an output widget, produced by the widget abbreviations above.
"""
w.children

display(w) #to display the widget
#Access current argument value

##ACCESS VALUES
w.kwargs #Option 1: only reflects the initial state — the values passed when the interactive widget was first created
w.result #Option 2: result of based on function logic, if function has return value this will be used to access it and later use on code
#Option 3: If you need to use the actual input values (not just the result), access the individual widget values
a_slider = w.children[0]
b_slider = w.children[1]

a = a_slider.value
b = b_slider.value

print(a, b)
#Option 4: If you want to react immediately when the user changes a value (like in an event-driven app), use .observe()

def on_change(change):
    a = w.children[0].value
    b = w.children[1].value
    print(f"Live values: a={a}, b={b}, sum={a + b}")
    # You can now use these values in your code

for slider in w.children:
    slider.observe(on_change, names='value')

#In summary, observe (like JS eventlistener) and result is best for values that you are displaying and children.values is best for values computed behind the scenes or in the function and needed or output later

