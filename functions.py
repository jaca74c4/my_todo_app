FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Pobiera zawartość pliku to-do i zwraca listę elementów."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Nadpisuje plik listą z nowymi wartościami."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
