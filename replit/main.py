import submenu

from week0 import matrix, movingcar, swap, tree
from week1 import infodb, fibonacci
from week2 import lcm, factorial

# from folder/subfolder import filename
main_menu = [
    ["Database", infodb.tester ]
]

sub_menu = [
    ["Moving Car", movingcar.ship],
    ["Tree", tree.tree]
]

math_sub_menu = [
    ["Number Swap", swap.numbswap],
    ["Matrix", matrix.matrix],
    ["Fibonacci", fibonacci.run],
    ["Factorial", factorial.tester],
    ["LCM", lcm.run]
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
