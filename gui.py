
#Sec- 16: GUI
# Third party modules

import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
# creates a text label on window... its not a string, but takes in a text instance
input_box = sg.InputText(tooltip="Enter todo")
# we have created these somewhere and not connected it to windows
add_button =sg.Button("Add")

window = sg.Window('My TO-DO App', layout=[[label ], [input_box, add_button]])
#creates window instance with elements
# Cafe-- In cafe you order a pizza .. but it makes coffee instances and tea, but don't make pizzas.
# they offera service.. they order a pizza from third party..from a pizza shop nearby.
# python doesnot have window object by7 default.. but we can get those object instance from other third parties
# PySimpleGUI => Pizza shop, Window("My to-do App") => actual pizza instance, "My to do App" => what pizza do you want

# layout is an argument and it expects a list... a list of object instances, buttons, textboxes.
# [[..]] => the items you put in inner square brackets will be placed in one row
# [[][]] => two rows with one item each.
# [[_ , _], [_]]  => row1 col2, row2 col1.

# nothing happens when you click on button, bcs you havn't added any actions/functions.Create
window.read()
# it displays window on the screen --- its a method not a function
window.close()

