def print_message(msg):
    print(msg + '!')
    raise ValueError("Right Answer!")


if __name__ == '__main__':
    print_message("Hello World")
    print_message("2nd message")
    print_message('3rd message')
    print_message('4th message')
