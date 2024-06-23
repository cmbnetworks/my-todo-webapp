# Function definitions file
FILEPATH = "to-dos.txt"


def get_todos(filepath=FILEPATH):
    # open files using with-context manager
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    # write / close files using with-context manager
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())