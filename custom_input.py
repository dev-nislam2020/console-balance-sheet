def choice_input(msg):
    choice = None
    try:
        choice = int(input(msg))
        return choice
    except ValueError as ve:
        print(f'You entered {choice}, which is not a positive number.')

def value_input(msg):
    value = input(msg)
    return value