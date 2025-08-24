from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

# Very basic function
def f(x):
    print("Hello")
    return x

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

#CONTINUE at using function annotations with interact