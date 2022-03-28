import submenu
from infodb import *
from lcm import *

main_menu = [
    ["Database", "infodb.py"]
]

sub_menu = [
    ["Moving Ship", "replit/week0/movingship.py"],
    ["Moving Car", "replit/week0/movingcar.py"],
    ["Tree", "replit/week0/tree.py"]
]

math_sub_menu = [
    ["Number Swap", "replit/week0/swap.py"],
    ["Matrix", "replit/week0/matrix.py"],
    ["Fibonacci", "replit/week1/fibonacci.py"],
    ["Factorial", "replit/week2/factorial.py"],
    ["LCM", "lcm.py"]
]

border = "=" * 25
banner = f"\n{border}\nSelect an option!\n{border}"


def menu():
    title = "Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Animations", submenus])
    menu_list.append(["Math", math_submenu])
    buildMenu(title, menu_list)


def submenuc():
    title = "submenu" + banner
    m = submenu.Menu(title, sub_menu)
    m.menu()


def submenus():
    title = "submenu" + banner
    buildMenu(title, sub_menu)


def math_submenuc():
    title = "submenu" + banner
    m = submenu.Menu(title, math_sub_menu)
    m.menu()


def math_submenu():
    title = "submenu" + banner
    buildMenu(title, math_sub_menu)


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
    choice = input("Input your choice> ")

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
