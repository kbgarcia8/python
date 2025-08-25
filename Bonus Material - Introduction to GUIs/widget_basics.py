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