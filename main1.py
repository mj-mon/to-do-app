# Sec: 7 Day: 7
# List-Comprehensions
# (71)


# removing backslash char from the list- w/ 1)loops and w/ 2)list-comprehensions
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo:") + "\n"

            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            #uSE with
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)


            # file = open('todos.txt', 'w')
            # file.writelines(todos)
            # file.close()

            with open('todos.txt', 'w') as file:
                 file.writelines(todos )

        case 'show':
            # file = open('todos.txt','r')
            # todos = file.readlines()
            # file.close()

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            # new_todos = []


            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            #shorter way to modify items in list-- list-comprehesionadd

            # new_todos  = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"

                print(row)


        case 'edit':
            number = int(input(" Number or the todo to edit:"))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            print("Here is existing todos", todos)

            new_todo = input("Enter a new todo:")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':

            number = int(input("Number or the todo to complete:"))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)


            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        case 'exit':
            break
print("Bye!")

