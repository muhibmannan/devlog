"""<DevLog — a personal developer productivity tool for the terminal.>"""

VERSION = "0.1.0"

MENU_OPTIONS = ["Add Task", "List Tasks", "Quit"]
SORT_BY = ["Priority", "Date Added", "Status", "Back"]



def show_menu():
    print()
    print("====================")
    print(f"   DevLog v{VERSION}")
    print("====================")
    print()
    for i, option in enumerate(MENU_OPTIONS):
        print(f"{i + 1}. {option}")


def get_user_choice():
    choice = input("\nEnter choice: ").strip()    # strip whitespace
    return choice



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

def sort_tasks():
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

def handle_choice(choice):
    if choice == "1":
        get_task_input()
        return True
    
    elif choice == "2":
        sort_tasks()
        return True
                
    elif choice == "3":
        print("\nGoodbye!")
        return False
    else:
        print("\nInvalid choice. Try again.")
        return True

def run():
    while True:
        show_menu()
        choice = get_user_choice()
        if not handle_choice(choice):
            break


def main():
    run()


if __name__ == "__main__":
    main()