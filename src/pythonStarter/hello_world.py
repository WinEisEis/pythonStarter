def print_message(msg):

    print(msg + '!')
    raise ValueError("Wrong Answer!")


if __name__ == '__main__':
    print_message("Hello World")