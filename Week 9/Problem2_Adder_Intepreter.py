all_vars = {}
error = "Syntax error."


def the_whole_shabang(usr_input):
    usr_input = usr_input.split()
    args = len(usr_input)

    if args == 2 and usr_input[0] == "print":
        print_cmd(usr_input)
    elif args == 1 and usr_input[0] == "quit":
        quit_cmd()
    elif args == 2 and usr_input[0] == "input":
        input_cmd(usr_input)
    elif args == 3 and usr_input[1] == "gets":
        gets_cmd(usr_input)
    elif args == 3 and usr_input[1] == "adds":
        adds_cmd(usr_input)
    else:
        print(error)


def quit_cmd():
    print("Goodbye.")
    exit()


def gets_cmd(usr_input):
    global all_vals

    try:
        if isinstance(usr_input[0], str) and isinstance(int(usr_input[2]), int):
            all_vars[usr_input[0]] = usr_input[2]
        else:
            print(error)
    except ValueError:
        if is_in_dict(usr_input[2]) is not False:
            all_vars[usr_input[0]] = is_in_dict(usr_input[2])
        else:
            print(error)


def print_cmd(usr_input):
    global all_vars

    try:
        print(str(usr_input[1]) + " equals " + str(all_vars[usr_input[1]]))
    except KeyError:
        print(usr_input[1] + " is undefined.")


def adds_cmd(usr_input):
    global all_vars

    try:
        if isinstance(usr_input[0], str) and isinstance(int(usr_input[2]), int):
            val = int(all_vars[usr_input[0]])
            adding = int(usr_input[2])
            all_vars[usr_input[0]] = val + adding
    except ValueError:
        if is_in_dict(usr_input[2]) is not False:
            adding_val = int(is_in_dict(usr_input[2]))
            all_vars[str(usr_input[0])] = int(is_in_dict(usr_input[0])) + adding_val
        else:
            print(error)
    except KeyError:
        print(usr_input[0] + " is undefined.")


def input_cmd(usr_input):
    global all_vars

    if isinstance(usr_input[1], str) and has_nums(usr_input[1]) is not True:
        val = input("Enter a value for " + str(usr_input[1]) + ": ")

        try:
            if verify_val(int(val)) is True:
                all_vars[usr_input[1]] = int(val)
        except ValueError:
            if is_in_dict(val) is not False:
                all_vars[usr_input[1]] = is_in_dict(val)
            else:
                print(error)


def has_nums(string):
    return any(i.isdigit() for i in string)


def is_in_dict(val):
    global all_vars

    if val in all_vars.keys():
        return all_vars.get(val)
    else:
        return False


def verify_val(arg):
    if int(arg) > 0:
        return True
    else:
        return False

# MAIN PROGRAM
script = input("Script name: ")

with open(script, "r") as f:
    content = f.read().split('\n')

    for line in content:
        the_whole_shabang(line)