# 1
# prompt = "Enter a todo:"
# user_text = input(prompt)
# print(user_text)

# 2 Select section + ctrl + / (t0 add comment)
# user_prompt = "Enter a todo:"
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)
#
# # Use Lists
#
#
# todos = [todo1,todo2,todo3]
# print(todos)
# print(type(user_prompt))
# print(type(todos))
# print(type(todo1))


# 3 Batch Operation - write fn once and Execute it multiple times

# user_prompt = "Enter a todo:"
#
# while True :
#     todo = input(user_prompt)
#     print(todo)
#     print("Next...")

#4 Add todos to a List

# user_prompt = "Enter a todo:"
#
# todos = []
#
# while True :
#     todo = input(user_prompt)
#     # print(todo.capitalize())
#     todos.append(todo)
#     # append is a method -are like functions , but attached to data types to other objects
#     # (it is part of the object(todos)(list type) associated with the variable
#     # every object has its own Method
#     # string does not have a append method
#     print(todos)


      # Using Help
      # help("mmkjkhh".capitalize)
      # dir(str)
      # to get a list of builtin functions >>> import builtins >>> dir(builtins)

#5   Section 3 (28) ..... How to make programs take decisions
                # Allow user what they want to do ... Add new todo or see to to
                # match case statement - available in python 3.8

todos = []
#
# while True:
#     user_action = input("Type add, show or exit: ")
#
#     match user_action:
#         case 'add':
#             todo = input("Enter a todo:")
#             todos.append(todo)
#         case 'show':
#             print(todos)
#         case 'exit':
#             break
# print("Bye!")


#6  3(29) Improving program output # for loop -- list without brackets and quotes


# todos = [] / when using file read method and string value in a list


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo:") + "\n"
            # to store items permanently use list
            # read the content and create a list with that content, each line will be item in that list
            file = open('todos.txt', 'r')
            todos = file.readlines()
            # it returns a list- same datatype as writing [] in python
            # normally list are created automatically from other external files
            file.close()

            todos.append(todo)

            # To store list items in a text file
            # create a new file and completely overwrite existing file
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()

            print(todos)
            # Use List-comprehensions to remove the backslash char
            for index, item in enumerate(todos):
                     #enumerate fn to access items  + indexes of the list
                     # ex; a = enumerate(["a", "b", "c"])
                     #     b = enumerate("Hello")
                     #     list(a)
                     #     list(b) and not str(b)
                # print(index, '-', item)

                 #simple solution to remove \n char -- in one line
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                     # fstrings
                print(row)
           #print("Length is", index + 1)
           #print(f"Length is {index + 1}")
           #print(len(todos))


        case 'edit':
            number = int(input(" Number or the todo to edit:"))
            # input fn always produces a string type - use int(), float()
            number = number - 1
            new_todo = input("Enter a new todo:")
              #existing_todo = todos[number]
              #print(existing_todo)
            todos[number] = new_todo
            # will use list-indexing system to be able to extract that item of the list which has an index of 2
        case 'complete':
            # we want to manipulate the list - so if the user completes the to-do we want to delete
            # help(list.remove)
            number = int(input(" Number or the todo to complete:"))
            todos.pop(number - 1)


        case 'exit':
            break
print("Bye!")

