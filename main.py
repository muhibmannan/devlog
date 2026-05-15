"""<DevLog — a personal developer productivity tool for the terminal.>"""

VERSION = "0.1.0"

MENU_OPTIONS = ["Add Task", "List Tasks", "Quit"]
SORT_BY = ["Priority", "Date Added", "Status", "Back"]

def show_banner():
    print("====================")
    print(f"   DevLog v{VERSION}")
    print("====================")


def display_menu():
    print()
    for i, option in enumerate(MENU_OPTIONS):
        print(f"{i + 1}. {option}")


def sort_menu_options():
    print()
    for i, option in enumerate(SORT_BY):
        print(f"{i + 1}. {option}")


def get_task_input():

    title = input("\nTask title: ").strip()

    if not title:
        print("Nothing was typed.")
        return

    while True:
        priority_input = input("Priority (1=low, 2=medium, 3=high): ").strip()
        if priority_input in ["1", "2", "3"]:
            priority = int(priority_input)
            break
        else:
            print("Invalid input. Please enter 1, 2 or 3.")
                   
    print(f"\nTask title: {title}, Priority level: {priority}")


def run():
    while True:
        display_menu()
        choice = input("\nEnter choice: ").strip()

        if choice == "":
            print("\nInvalid choice. Try again.")
        elif choice == "1":
            get_task_input()
        elif choice == "2":
            while True:
                sort_menu_options()
                sort_choice = input("\nSorting by: ").strip()
                
                if sort_choice == "4":
                    break
                elif sort_choice in ["1", "2", "3"]:
                    print(f"\n[Sorting by {SORT_BY[int(sort_choice) - 1]} - coming soon]")
                    break 
                else:
                    print("\nInvalid choice. Try again.")
        elif choice == "3":
            print("\nGoodbye!")
            break


def main():
    show_banner()
    run()


if __name__ == "__main__":
    main()