Filename = "../Web_app/todos.txt"

def read_todo(filename = Filename):
    """Reads the items of the todos storage file into a LIST format"""
    with open(Filename, "r") as file:
        todos_local = file.readlines()
        return todos_local

def write_todo(todo_arg,filename = Filename):
    """Writes any new or edited values into the todos storage file"""
    with open(Filename, "w") as file:
        file.writelines(todo_arg)

