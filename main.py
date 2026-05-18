"""<DevLog — a personal developer productivity tool for the terminal.>"""

VERSION = "0.1.0"

MENU_OPTIONS = ["Add Task", "List Tasks", "Quit"]
SORT_BY = ["Priority", "Date Added", "Status", "Back"]



def show_banner():
    print()
    print("====================")
    print(f"   DevLog v{VERSION}")
    print("====================")

def show_menu():
    print()
    for i, option in enumerate(MENU_OPTIONS):
        print(f"{i + 1}. {option}")

def get_menu_choice():
    raw= input("\nChoose an option: ").strip()
    if not raw.isdigit():
        return None
    value = int(raw)
    if value not in {1, 2, 3}:
        return None
    return value

def parse_task_input(raw_text):
    cleaned = raw_text.strip()
    if cleaned == "":
        return "", False
    return cleaned, True

def get_task_input():
    raw = input("\nTask title: ")
    title, valid = parse_task_input(raw)

    if not valid:
        print("Nothing was typed.")
        return None

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
        print()
        for i, option in enumerate(SORT_BY):
            print(f"{i + 1}. {option}")
        sort_choice = input("\nSorting by: ").strip()
        if sort_choice == "4":
            break
        elif sort_choice in ["1", "2", "3"]:
            print(f"\n[Sorting by {SORT_BY[int(sort_choice) - 1]} - coming soon]")
            break 
        else:
            print("\nInvalid choice. Try again.")

def confirm_action(prompt):
    response = (input(prompt)).strip().lower()
    return response in ["y", "yes"]

def handle_choice(choice):
    if choice == 1:
        get_task_input()
        return True
    elif choice == 2:
        sort_tasks()
        return True        
    elif choice == 3:
        if confirm_action("Are you sure you want to quit? (y/n): "):
            print("\nGoodbye!")
            return False
        return True
    else:
        print("\nInvalid choice. Try again.")
        return True
    

def run():
    while True:
        show_menu()
        choice = get_menu_choice()
        if choice is None:
            print("Invalid choice, try again.")
            continue
        if not handle_choice(choice):
            break

def main():
    show_banner()
    run()


if __name__ == "__main__":
    main()