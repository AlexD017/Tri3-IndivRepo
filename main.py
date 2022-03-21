import submenu


main_menu = [
    ["Number Swap", "replit/swap.py"],
    ["Matrix", "replit/matrix.py"],
    ["Lists", "replit/dbhack.py"],
    ["Fibonacci Sequence", "replit/fibonacci.py"] 
]

sub_menu = [
    ["Moving Ship", "replit/movingship.py"],
    ["Moving Car", "replit/movingcar.py"],
    ["Tree", "replit/tree.py"]
]

border = "=" * 25
banner = f"\n{border}\nSelect an option!\n{border}"


def menu():
    title = "Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Animations", submenua])
    buildMenu(title, menu_list)


def submenus():
    title = "Submenu" + banner
    m = submenu.Menu(title, sub_menu)
    m.menu()


def submenua():
    title = "Submenu" + banner
    buildMenu(title, sub_menu)


# builds console menu
def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user input
    choice = input("input your choice> ")

    # Process user input
    try:
        choice = int(choice)
        if choice == 0:
            # stops
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                # check main_menu dictionary
                print(f"file not found!: {action}")
    except ValueError:
        # not a number
        print(f"not a number: {choice}")
    except UnboundLocalError:
        # not one of the numbers listed
        print(f"invalid choice: {choice}")

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
