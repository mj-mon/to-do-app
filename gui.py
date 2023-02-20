
#Sec- 16: GUI
# Third party modules

import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
# creates a text label on window... its not a string, but takes in a text instance
input_box = sg.InputText(tooltip="Enter todo", key="todo")
# we have created these somewhere and not connected it to windows
add_button =sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window('My TO-DO App',
                   layout=[[label ], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))
#creates window instance with elements
# Cafe-- In cafe you order a pizza .. but it makes coffee instances and tea, but don't make pizzas.
# they offera service.. they order a pizza from third party..from a pizza shop nearby.
# python doesnot have window object by7 default.. but we can get those object instance from other third parties
# PySimpleGUI => Pizza shop, Window("My to-do App") => actual pizza instance, "My to do App" => what pizza do you want

# layout is an argument and it expects a list... a list of object instances, buttons, textboxes.
# [[_._._]] => the items you put in inner square brackets will be placed in one row
# [[][]] => two rows with one item each.
# [[_ , _], [_]]  => row1 col2, row2 col1.
# [[_],[_,_]] => roq1 col1, row2 col2
# [[_],[_],[_]] => 2 rows > list of three lists.

# nothing happens when you click on button, bcs you havn't added any actions/functions.Create
#event = window.read()
while True:
    # While loop --> so the app d/n close on pressing add button
    event, values = window.read()
    #method read returns tuple
    print(1, event)
    # event = todos

    print(2, values)
    # value = dictionary
    # user has selected the values currently
# it displays window on the screen --- its a method not a function
    print(3, values['todos'])
    # ['todos'] is a list.
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            # we point to the listbox instance and point to the
            # ...method of that listbox instance and say values=todos
            # the updated todos will have new_todos added

        case "Edit":
            todo_to_edit = values['todos'][0]
            # the dictionary is values which we printed
            # we want to get ['ihhihjhdjh\n'] > we point to
            # todos key. to get actual string [0]

            new_todo = values['todo']

            todos = functions.get_todos()
            # to replace existing item in the list
            index = todos.index(todo_to_edit)
            # to update todos list with new to-do
            todos[index] = new_todo
            functions.write_todos(todos)
            # write_todos modifies todos.txt files

            window['todos'].update(values=todos)
            # point to list box key [todos]
            # will give us the list box instance

    # when we select a list item from GUI it should reflect in the text box
    # when we select  a to-do item ex: clean --> the event is todos that has
        # the key of the Listbox key='todos'
    # therefore in match case we want to capture that.

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
        #new list will be written in the file

window.close()

