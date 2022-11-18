USERS = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This contact doesnt exist, please try again.'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'This contact cannot be added, it exists already'
        except TypeError:
            return 'Unknown command or parameters, please try again.'
    return inner


@input_error
def add_user(args):
    name, phone = args
    USERS[name] = phone
    return f"User {name} added"

@input_error
def change_phone(args):
    name, phone = args
    old_phone = USERS[name]
    USERS[name] = phone
    return f"User {name} have a new phone number {phone}, old was: {old_phone}"

@input_error
def show_number(args):
    user = args[0]
    phone = USERS[user]
    return f"{user}: {phone}"

def show_all(_):
    result = ""
    for name, phone in USERS.items():
        result += f"{name}: {phone}\n"
    return result

def hello(_):
    return "How can I help you?"


HANDLERS = {
    "hello": hello,
    "add": add_user,
    "change": change_phone,
    "show": show_all,
    "phone": show_number,
}

EXIT_COMMANDS = ("exit", "close", "good bye")


def parser_input(user_input):
    cmd, *args = user_input.split()
    handler = HANDLERS[cmd.lower()]
    return handler, args

#@input_error
def main():
    while True:
        user_input = input(">>>")
        if user_input.lower() in EXIT_COMMANDS:
            print("Good bye!")
            break

        try:
            handler, *args = parser_input(user_input)
            result = handler(*args)
        except KeyError:
            result = f'Unknown command "{user_input}", please try again.'

        print(result)


if __name__ == "__main__":
    main()
